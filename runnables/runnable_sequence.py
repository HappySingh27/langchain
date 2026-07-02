from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv

prompt1 = PromptTemplate(
    template='write a joke on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain this joke {text}',
    input_variables=['text']
)


model = ChatOpenAI()
parser= StrOutputParser()

# | (pipe) operator is just a clean way of writing Runnable Sequence
chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)
result = chain.invoke({'topic':'RunnableSequence explain kro'})

print(result)