"""
CSVLoader : 
    - CSVLoader is a document loader used to load csv files into langChain Document objects - 
    one per row, by default

- we can create our own custom data loader - refer langchain documentation
"""

from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='annual-enterprise-survey-2025-financial-year-provisional-size-bands.csv')

docs = loader.load()

print(len(docs))
print(docs[0].page_content)