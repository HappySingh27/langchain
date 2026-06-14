"""
Chat Model vs Traditional Model:

Traditional Model:
- Developer manually maintains chat history
- Stitches text together manually
- Formats structural markers (User:, Bot:) as raw text string

Chat Model:
- Interprets conversation history more intelligently
- Trained to understand start/end tokens
- Recognizes role boundaries automatically
- Keeps context separated correctly
- Knows exactly when to stop

Key Distinction:
While chat history can be maintained in both models, only the chat model
is trained to understand the start and end tokens of system, user, and AI
messages, resulting in vastly superior outputs.
"""

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=1.5, max_completion_tokens=50)
result = model.invoke("Prompt")


print(result)
