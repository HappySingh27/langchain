from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

#dimension - higher the dimension higher the cost and contextual meaning
embedding = OpenAIEmbeddings(model='enter-model-name', dimensions=32)

result = embedding.embed_query("Delhi is the capital of India")

print(str(result))