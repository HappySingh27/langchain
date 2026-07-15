from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# Creating 5 Document objects
docs = [
    Document(page_content="Text content from the first part of the image...", metadata={"source": "screenshot", "page": 1}),
    Document(page_content="Text content from the second part of the image...", metadata={"source": "screenshot", "page": 2}),
    Document(page_content="Text content from the third part of the image...", metadata={"source": "screenshot", "page": 3}),
    Document(page_content="Text content from the fourth part of the image...", metadata={"source": "screenshot", "page": 4}),
    Document(page_content="Text content from the fifth part of the image...", metadata={"source": "screenshot", "page": 5})
]

"""
# Display the documents
for i, doc in enumerate(docs):
    print(f"Document {i+1}:")
    print(f"Content: {doc.page_content[:50]}...")
    print(f"Metadata: {doc.metadata}\n")
"""

# creating a vectore store
vector_store = Chroma(
    # OpenAIEmbeddings() would be used for generating embeddings
    embedding_function=OpenAIEmbeddings(),
    # the filesystem path where the vector store saves its on-disk data
    persist_directory="./chroma_db",
    collection_name='sample'
)

# add documents
vector_store.add_documents(docs)

# get documents
embedd_data = vector_store.get(include=['embeddings','documents','metadatas'])
#print(embedd_data)

# searching data
data = vector_store.similarity_search(
    query='second',
    k=2
)
#print(data)

# search data and get similarity score as well
vector_store.similarity_search_with_score(
    query='third',
    k=2
)

# filter using meta-data
data=vector_store.similarity_search_with_score(
    query='',
    filter={'source':'screenshot'}
)
#print(data)

vector_store.delete()