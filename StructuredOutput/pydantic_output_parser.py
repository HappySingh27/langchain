"""
PYDANTIC OUTPUT PARSER - Structured Output with Schema Validation

What is PydanticOutputParser?
PydanticOutputParser is a structured output parser in LangChain that uses Pydantic models to 
enforce schema validation when processing LLM responses.

Why Use PydanticOutputParser?
✓ Strict Schema Enforcement → Ensures that LLM responses follow a well-defined structure
✓ Type Safety → Automatically converts LLM outputs into Python objects (Pydantic instances)
✓ Easy Validation → Uses Pydantic's built-in validation to catch incorrect or missing data
✓ Seamless Integration → Works well with other LangChain components

Key Differences from JsonOutputParser:
- JsonOutputParser: JSON string → Python dict (no type validation)
- PydanticOutputParser: JSON string → Pydantic model instance (with type validation & enforcement)

When to Use:
- When you need strict type checking and field validation
- When output structure is critical and must follow a schema
- When you want IDE autocomplete and type hints
- For production systems requiring data integrity
"""

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import json

load_dotenv()

# Step 1: Define Pydantic Model (enforces schema)
class Person(BaseModel):
    """Pydantic model defines the expected structure of LLM output"""
    name: str = Field(description="Name of the person")
    age: int = Field(description="Age of the person")
    city: str = Field(description="City where person lives")

# Step 2: Create parser with the Pydantic model
parser = PydanticOutputParser(pydantic_object=Person)

# get_format_instructions():
# - Returns ready-made text instructions for the LLM.
# - Includes the schema from the Person Pydantic model.
# - Helps the LLM return JSON that can be converted into a Person object.

# Step 3: Create LLM endpoint
llm = HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V4-Pro',
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

# Step 4: Create prompt template with format instructions
template = PromptTemplate(
    template='Generate a fictional person with name, age, and city.\n{format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# Step 5: Format prompt
# format():
# - Builds the final prompt string from the PromptTemplate.
# - Replaces placeholders using input_variables and partial_variables.
# - Here, it inserts parser.get_format_instructions() into {format_instruction}.
prompt = template.format()

# Step 6: Get LLM response
result = model.invoke(prompt)

# Step 7: Parse response using PydanticOutputParser
parsed_result = parser.parse(result.content)

# Step 8: Use parsed result (now it's a Pydantic object, not a dict!)
print("Parsed Result (Pydantic object):")
print(parsed_result)
print(f"\nType: {type(parsed_result)}")
print(f"Name: {parsed_result.name}")
print(f"Age: {parsed_result.age}")
print(f"City: {parsed_result.city}")
