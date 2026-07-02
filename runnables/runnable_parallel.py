"""
Runnable Prallel is a runnable primitive that allows multiple runnables to execute in parallel
Each runnable receives the same input and process it independently, producing a dictionary of output

Goal : Same Input to 2 different runnables one generate twitter post another generate linkedIn Post
"""

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template='generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='generate a linkedIn Post about {topic}',
    input_variables=['topic']
)

# creating object of ChatOpenAI
model = ChatOpenAI()

# creating object of StrOutputParser
parser = StrOutputParser()

# making parallel chains, initialize by giving dictionary as input
chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1,model,parser),
    'linkedIn': RunnableSequence(prompt2,model,parser)
})

result = chain.invoke({'topic':'Average package of and AI Engineer with 3+ YOE'})

print(result)
print(result['tweet'])
print(result['linkedIn'])