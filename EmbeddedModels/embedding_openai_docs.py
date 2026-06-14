from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

#dimension - higher the dimension higher the cost and contextual meaning
embedding = OpenAIEmbeddings(model='enter-model-name', dimensions=32)

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Wengal",
    "Paris is the capital of France"
]

result = embedding.embed_documents(documents)

print(str(result))