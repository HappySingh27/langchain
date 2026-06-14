"""
Three types of messages available in Langchain
    1. System message
    2. Human message
    3. AI message

invoke() method
    1. single message (single turn stand alone queries)
        a. static message
        b. dynamic message
            i. prompt template
    2. list of messages (multi-turn conversation)
        a. static message
            i.   SystemMessage
            ii.  HumanMessage
            iii. AImessage
        b. dynamic message
            i. ChatPromptTemplate
    """


from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

messages = [SystemMessage(content='You are my friend ganesha'),
            HumanMessage(content='Kripa banye rankhein')]

#impliment chat history here 
while True:
    user_input = input('You: ')
    if user_input == 'exit':
        break
    messages.append(HumanMessage(content=user_input))
    result = model.invoke(messages)
    print('result AI:',result.content)
    messages.append(AIMessage(content=result.content))
    print()