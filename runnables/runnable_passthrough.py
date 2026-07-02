"""
RunnablePassthrough is a special runnable primitive that simply the input as output
without modifying it.
"""

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough

load_dotenv()

passthrough = RunnablePassthrough()

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


# below is the example of using Runnable Passthrough, becuase I wanted to print joke also,
# before explanation
chain = RunnableSequence(
    RunnableSequence(prompt1, model, parser),
    RunnableParallel({
        'joke':RunnablePassthrough(),
        'explain':RunnableSequence(prompt2, model, parser)}))

result = chain.invoke({'topic':'langchain'})
print(result)