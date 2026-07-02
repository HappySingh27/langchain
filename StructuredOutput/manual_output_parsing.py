"""
Types of Output Parsers;-
a. StrOutputParser
b. JSONOutputParser
c. StructuredOutputParser
d. Pydantic Output Parser

topic -> LLM -> [Detailed Report] -> LLM -> 5 line summary

"""

import os
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate

os.environ["HF_HOME"] = "/Users/happysingh/Documents/happy_projects/langchain/hf_cache"

llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 100,
    },
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template = 'Write a detailed report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template = 'Write a 5 summary on the following. /n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic' : 'black hole'})

text = model.invoke(prompt1).content

prompt2 = template2.invoke({'text': text})

result = model.invoke(prompt2)

print('---------------------------')
print(result.content)
print('---------------------------')