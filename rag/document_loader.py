"""
Document Loaders are the components in Langchain used to load data from various sources
into a standarized format usually a (Documents objects) which then can be used for chunking 
embedding, retrieval and generation.

Many tupes of Document Loader are  there, all document loader lie in
langachain_community(this is depricated now) package

Loader converts docs in list of docs

Some Loaders :
1. Text Loaders
2. PDF Loader
    - There are multiple pdf loader available in langchain , to work 
      with different types of data like pdf of images
3. Directory Loader
4. Load vs Lazy Load
    - Lazy Load : returns generator, with it's help laods one doc at once in memory
    vs
    - Load : Load all docs in one go in mone memory
5. CSV Loader
6. Other Document Loader
7. Custom Document Loader
8. Web Base Loader
9. Langchain almost has Document Loader for every thing like Amazaon cloud, youtube etc.

No matter in whihc format data we have loaded it would always be converted to
Document format in Langchain

"""

from langchain_community.document_loaders import TextLoader

# many sort of param can be passed in the TextLoader()
# for now passing path of the file to be loaded
loader = TextLoader('movie_review.txt', encoding='utf-8')

docs = loader.load()

print(docs)
