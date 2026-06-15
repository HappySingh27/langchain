"""
2 types of LLM based on output
    a. LLMs which can return structured output
        i. Need to define structure of output data before invoking model
           with the help of with_structured_output() function
            a. with_structured_output() - define data format with this function
               using below 3 ways
                1. Pydantic
                2. Typed Dictionaries
                3. json_schema
                
    b. LLMs which cannot return structured output
        i. Langchain provides output parsers classes to convert data in a 
           particular structure

"""

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal

load_dotenv()

model = ChatOpenAI()

#schema for output data
class Review(TypedDict):

    """
    summary: str
    sentiment: str
    """

    # giving context to llm for avoiding any hallucination
    # using Annotated
    key_themes: Annotated[list[str],'Write down key themes of review']
    summary: Annotated[str,'A brief summary of the review']
    sentiment: Annotated[str,'Return sentiment of review']
    pros: Annotated[Optional[list[str]],'Write all pros']
    cons: Annotated[Optional[list[str]],'Write all cons']

#methods responsible for returning structured data
structured_model = model.with_structured_output(Review) 
result = structured_model.invoke("Javan is not so good Movie")

print(result)
print(result['summary'])
print(result['sentiment'])