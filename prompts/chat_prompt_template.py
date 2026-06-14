"""
Message Placeholder in langchain :
In LangChain, a MessagesPlaceholder is a specialized prompt template
component used to dynamically insert a list of full chat messages
(like chat history or agent scratchpads) into a specific position
within a prompt, used to give chat bot when user comes back after 
some time to check status of query, when starting a new chat, 
here we store chat history in db and then pull it from db to give context to chatbot
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

"""
chat_template = ChatPromptTemplate([
    SystemMessage(content='you are a helpfull {domain} domain expert'),
    HumanMessage(content='Explain in simple terms, what is {topic}')

])
"""
chat_template = ChatPromptTemplate([
    ('system','you are a helpfull {domain} domain expert'),
    ('human','Explain in simple terms, what is {topic}')]
)


chat = chat_template.invoke({'domain':'cricket',
'topic':'Doosra'
})

print(chat)

