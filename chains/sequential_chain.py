"""
SEQUENTIAL CHAIN IN LANGCHAIN

Goal:
- Learn how to connect multiple steps where the output of one step becomes
  the input of the next step.

Basic flow:
Prompt 1 -> Model -> Parser -> Prompt 2 -> Model -> Parser

Meaning:
1. First prompt creates a detailed answer.
2. First model call generates the detailed text.
3. Parser converts the AIMessage into a plain string.
4. Second prompt receives that string and asks for a summary.
5. Second model call generates the final summarized answer.
6. Final parser again returns clean text.
"""

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


# Loads API keys and environment variables from the .env file.
load_dotenv()


# ChatOpenAI is the LLM wrapper.
# Same model can be used multiple times inside one chain.
model = ChatOpenAI()


# Parser converts AIMessage output into a plain Python string.
# This is important because the next prompt expects normal text as input.
parser = StrOutputParser()


# First prompt:
# Takes a topic from the user and asks the model to create detailed content.
template1 = PromptTemplate(
    template="Write a detailed explanation about {topic}.",
    input_variables=["topic"],
)


# Second prompt:
# Takes the output from the first chain step as {text}.
# This prompt asks the model to summarize that detailed text.
template2 = PromptTemplate(
    template="Summarize the following text in 5 simple bullet points:\n{text}",
    input_variables=["text"],
)


# Sequential chain:
# Data moves from left to right.
# 1. template1 uses {"topic": "..."} to create the first prompt.
# 2. model generates a detailed response.
# 3. parser extracts only the text from the AIMessage.
# 4. template2 receives that text in its {text} placeholder.
# 5. model generates the summary.
# 6. parser extracts the final clean summary string.
chain = template1 | model | parser | template2 | model | parser


# invoke() starts the full sequence.
# We only pass topic because template1 is the first step.
# The output from template1/model/parser is automatically passed to template2.
result = chain.invoke({"topic": "LangChain sequential chains"})


print(result)


# For visualization of the chain flow in terminal.
chain.get_graph().print_ascii()


"""
Same logic without using a sequential chain:

prompt1 = template1.invoke({"topic": "LangChain sequential chains"})
response1 = model.invoke(prompt1)
detailed_text = parser.invoke(response1)

prompt2 = template2.invoke({"text": detailed_text})
response2 = model.invoke(prompt2)
summary = parser.invoke(response2)

print(summary)

Why sequential chains are useful:
- They break a big task into smaller steps.
- Each step can transform the previous output.
- They make workflows like generate -> summarize, extract -> format,
  or research -> answer easy to build.
"""
