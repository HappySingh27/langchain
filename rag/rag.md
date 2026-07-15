# Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation (RAG) is an AI framework used to improve the accuracy and reliability of large language models (LLMs). It works by fetching facts from an external, authoritative knowledge base—such as company documents or a database—before generating a response, which helps ground the model and prevents it from hallucinating. 

## How RAG Works
Unlike a standalone model that relies solely on its pre-existing training data, a RAG-based system operates in three main steps:
1. **Retrieval:** When you ask a question, the system searches your external documents, PDFs, or databases for the most relevant pieces of information. 
2. **Augmentation:** The system takes your original question and adds the retrieved context to it, creating a highly specific and factual prompt.
3. **Generation:** The language model reads the augmented prompt and uses the provided, verified information to craft an intelligent, accurate answer.

## Key Benefits
RAG is highly favored by organizations and developers because it solves major issues inherent in standard AI models:
* **Reduces Hallucinations:** Because the AI draws from real, specific documents, it is much less likely to make up false information.
* **Access to Private Data:** It allows you to query your proprietary or internal data without needing to publicly expose or share it with the AI's training base.
* **Bypasses Retraining:** It eliminates the need to undergo expensive and time-consuming fine-tuning or retraining every time new data is added to your business. 

## Common Use Cases
* **Enterprise Chatbots:** Grounding customer service or internal helpdesk bots in verified company policies and FAQs.
* **Research and Summarization:** Enabling AI assistants to parse through massive archives of legal, medical, or financial documents to summarize specific findings.
* **Real-time Question Answering:** Using up-to-date databases to provide accurate, context-aware responses tied to a constantly changing knowledge base.

## Components
1. Document Loader
2. Text Splitter
3. Vector Databases
4. Retrievers

## Todo
1. Learn fine tuning theory & practical both, advantages, disadvantages, limitations, use cases
2. In context learning
    - In-Context Learning is a core capability of Large Language Models (LLMs) like
    GPT-3/4, Claude, and Llama, where the model learns to solve a task purely by seeing examples in the
    prompt—without updating its weights.