"""
SIMPLE CHAIN IN LANGCHAIN

Goal:
- Learn how to connect a prompt, model, and parser using the pipe operator: |

Basic flow:
PromptTemplate -> Model -> OutputParser

Meaning:
1. PromptTemplate creates the final prompt.
2. Model sends that prompt to the LLM.
3. StrOutputParser extracts clean text from the model response.
"""

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


# Loads API keys and environment variables from the .env file.
load_dotenv()


# ChatOpenAI is the LLM wrapper.
# It sends our prompt to the OpenAI chat model and returns an AIMessage object.
model = ChatOpenAI()


# PromptTemplate is used when the prompt has placeholders.
# {topic} is a placeholder that will be filled when we call chain.invoke().
template = PromptTemplate(
    template="Explain {topic} in 5 simple bullet points.",
    input_variables=["topic"],
)


# StrOutputParser converts the model response into a plain Python string.
# Without this parser, model.invoke() returns an AIMessage object.
parser = StrOutputParser()


# Simple chain:
# The pipe operator connects each step from left to right.
# Step 1: template receives {"topic": "..."} and creates the final prompt.
# Step 2: model receives the prompt and generates an answer.
# Step 3: parser receives the AIMessage and returns only the text content.
chain = template | model | parser


# invoke() runs the complete chain.
# The dictionary key must match the template placeholder name: topic.
result = chain.invoke({"topic": "LangChain chains"})


print(result)

# for visualization of chains
chain.get_graph().print_ascii()

"""
Same code without chain:

prompt = template.invoke({"topic": "LangChain chains"})
response = model.invoke(prompt)
result = parser.invoke(response)

print(result)

Why chain is useful:
- It keeps code short and readable.
- It clearly shows the flow of data.
- More steps can be added easily using another pipe.
"""
