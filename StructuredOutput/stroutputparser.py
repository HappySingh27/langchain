"""
# 📜 LANGCHAIN PARSERS VS. PYTHON VARIABLES (SHORT NOTES)

### 1. The Core Secret: LLMs Do NOT Return Strings
* In LangChain, calling `model.invoke()` returns a heavy **`AIMessage`** object, NOT a raw string.
* **The Object Structure:** `AIMessage(content="Actual text", response_metadata={...})`
* The actual text you want is trapped inside the `.content` property.

### 2. What is `StrOutputParser` Doing?
* It acts as a data cleaner on the automated conveyor belt (`|`).
* It extracts the `.content` string from the `AIMessage` and throws away the metadata.
* This ensures the next step in your pipeline receives a clean, raw Python string.

### 3. Why Use a Pipeline Parser Over Standard Variables?
You *can* write standard line-by-line Python using standard variables (`text = response.content`). However, using the pipeline (`|`) with a parser/lambda provides enterprise benefits:
* 🌊 **Streaming:** Parsers process text token-by-token in real-time. Standard variables cannot hold data until the model finishes completely.
* 🔀 **Parallel execution:** LangChain pipelines can run multiple prompts simultaneously out-of-the-box.
* 🤖 **Model Portability:** It normalizes data formats across different providers (OpenAI, HuggingFace, Anthropic).

### 4. Replacing the Parser with a Variable (The Java-Style Lambda Trick)
If you want to keep the pipeline layout but avoid importing the `StrOutputParser` module, replace it using a Python **Lambda expression** (conceptually identical to Java 8+ lambdas):

```python
# 'x' is the incoming AIMessage object. 
# The lambda instantly extracts and returns the string content.
chain = template1 | model | (lambda x: x.content) | template2 | model
```

"""


from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

template1 = PromptTemplate(
    template='Write a detailed report on {topic} ',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template = 'Write a 10 words summary on the following. \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic' : 'black hole'})

print(result)