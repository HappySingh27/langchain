"""
1. WebBaseLoader : 
    - WebBaseLoader is a document loader in LangChain used to load and extract text from
    web pages (URLs).
    - It uses BeautifulSoup under the hood to parse the HTML and extract visible text.

    Limitations ;
     - Does not handle javascript heavy pages well (use SeleniumURLLoader for that)
     - Loads only static content (what's in the HTML, not what loads after the renders).

"""

from langchain_community.document_loaders import WebBaseLoader

url = 'https://www.flipkart.com/'

loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))
print(docs[0].page_content)

"""
Todo :
    - Write a program which extract text from web pass it to ChatModel & ask 
    question regarding the same text
"""