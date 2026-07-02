"""
Runnable Lambda is a runnable primitive that allows you to apply custom python functions
within an AI pipeline.

It acts as middleware between different AI components, enabling preprocessing, transformation,
API calls, filtering and post processing in a Langchain workflow.

Runnablambda is used to add custom logic in chains.
"""

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnableLambda

load_dotenv()

def word_counter(text):
    return len(text.split())

runnable_word_counter = RunnableLambda(word_counter)

# print(runnable_word_counter.invoke("Hi my name is Happy Singh"))

prompt1 = PromptTemplate(
    template='Write a joke on your self {topic}',
    input_variables=['topic','Jerry']
)

model = ChatOpenAI()
parser = StrOutputParser()

chain = RunnableSequence(prompt1,model,parser,runnable_word_counter)

result = chain.invoke({'topic':'Claude'})

print(result)

