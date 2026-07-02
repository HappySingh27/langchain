from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema


"""
StructuredOutputParser is deprecated langchain 1.x version,
use pydantic parser instead

"""