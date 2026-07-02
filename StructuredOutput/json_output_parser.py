"""
LANGCHAIN PARSERS - How They Work:

1. LLM Output: Always returns TEXT/STRING, regardless of format
   - Even if you ask for JSON, it's still a string: '{"key": "value"}'
   
2. Parser's Role: Convert that text string into Python objects
   - JsonOutputParser: JSON string → Python dict
   - StrOutputParser: Any string → String (no conversion)
   - PydanticOutputParser: JSON string → Pydantic model instance
   
3. Parser Requirements:
   - Works ONLY when LLM returns structured data in expected format
   - Must explicitly instruct LLM to return JSON/CSV/structured format
   - If LLM returns plain text, parser fails (unless using StrOutputParser)
   - Incase llm returns unstructured data, programmers has to process it and
     convert it into structured data, so this conversion can be done on any 
     type of data not only the one returned by llm, we can proccess a text file 
     also can convert it to required type like json or pydantic object
   
4. Example Flow:
   LLM returns: '{"title": "Report", "body": "Content"}'  (string)
   ↓
   JsonOutputParser processes it
   ↓
   Python dict: {"title": "Report", "body": "Content"}  (usable object)

5. Limitation of JsonParser
    - output can be returned in json but we cannot enforce a schema in which
      output would be returned, StructuredOutputParser solves this problem,
      with it we can enforce schema in which we want our output
"""

from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V4-Pro',
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

# get_format_instructions():
# - Returns ready-made text instructions for the LLM.
# - Tells the LLM what output format the parser expects.
# - For JsonOutputParser, it asks the LLM to return valid JSON.

# 1st prompt Detailed report
# input_variables: List of placeholder names that USER must provide when calling template.format() or chain.invoke()
# partial_variables: Dict of placeholder names with VALUES that are pre-filled automatically (no user input needed)
template = PromptTemplate(
    template = 'Give me the name,age and city of fictional person \n {format_instruction}',
    input_variable=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# format():
# - Fills the prompt template placeholders with actual values.
# - Here, {format_instruction} is filled from partial_variables.
# - Returns the final prompt string that is sent to the LLM.
prompt = template.format()
result = model.invoke(prompt)
final_result = parser.parse(result.content)

"""
above 3 lines can also be written as 
chain = template | model | parser
result = chain.invoke({}) - sending blank dict because input_variable in 
template is empty, this is mandatory paran in chain.invoke() method
""" 

print(final_result)
print(type(final_result))
print(final_result['name'])


