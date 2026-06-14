from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

model = ChatOpenAI()

messages = [
    SystemMessage(content='You are my friend'),
    HumanMessage(content='Tell me about my future')
]

result=model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)