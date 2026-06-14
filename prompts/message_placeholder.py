from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


# chat template 

template = ChatPromptTemplate(
    [('system','you are helpfull customer support agent'),
     MessagesPlaceholder(variable_name='chat_history'),
     ('human','{query}')]
)

# load chat history
chat_history = []
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

result = template.invoke({
    'chat_history':chat_history,
    'query':'where is my refund'
})

print(result)

# create prompt