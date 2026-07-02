"""
CONDITIONAL CHAIN IN LANGCHAIN - a chain that routes input to different paths based on a condition

Goal:
- Learn how to route user feedback into different responses based on sentiment.
- Flow:
  1. User gives feedback.
  2. Model performs sentiment analysis.
  3. If sentiment is positive, send it to a happy response branch.
  4. If sentiment is negative, send it to a concern/escalation branch.

Basic flow:
Feedback -> Sentiment analysis -> Condition check -> Response branch -> Final reply

Meaning:
1. The first step classifies feedback as positive or negative.
2. The second step keeps the original feedback and the sentiment together.
3. The branch checks the sentiment value.
4. Positive feedback gets a thank-you style reply.
5. Negative feedback gets an apology and escalation style reply.
6. Pydantic keeps the sentiment output in a strict one-word field.
"""

from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnableParallel
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import Literal


# Loads API keys and environment variables from the .env file.
load_dotenv()


# One model can handle both sentiment analysis and response generation.
model = ChatOpenAI()


# Parser converts the final reply into plain text.
text_parser = StrOutputParser()


# Pydantic model keeps sentiment strict.
# The LLM must return only one of these two values.
class SentimentResult(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Return only one word: positive or negative"
    )


# Parser converts the sentiment analysis into a structured Pydantic object.
sentiment_parser = PydanticOutputParser(pydantic_object=SentimentResult)


# Step 1: classify the feedback as only positive or negative.
# The model should return just one word so the next step is easy.
sentiment_prompt = PromptTemplate(
    template=(
        "Analyze the sentiment of this customer feedback.\n"
        "{format_instruction}\n\n"
        "Feedback: {feedback}"
    ),
    input_variables=["feedback"],
    partial_variables={"format_instruction": sentiment_parser.get_format_instructions()},
)


# Step 2: positive reply prompt.
# This branch should sound warm, thankful, and helpful.
positive_reply_prompt = PromptTemplate(
    template=(
        "Customer feedback:\n{feedback}\n\n"
        "Sentiment: {sentiment}\n\n"
        "Write a friendly customer reply thanking them for the positive feedback."
    ),
    input_variables=["feedback", "sentiment"],
)


# Step 3: negative reply prompt.
# This branch should apologize, reassure the customer, and mention escalation.
negative_reply_prompt = PromptTemplate(
    template=(
        "Customer feedback:\n{feedback}\n\n"
        "Sentiment: {sentiment}\n\n"
        "Write a customer support reply that apologizes, shows concern, "
        "and says we are escalating the case to the right team."
    ),
    input_variables=["feedback", "sentiment"],
)


# Helper chain:
# This keeps the original feedback and also adds the sentiment label.
# We need both values later when building the final response.
analysis_chain = RunnableParallel(
    feedback=lambda x: x["feedback"],
    sentiment=sentiment_prompt | model | sentiment_parser,
)


# Condition function:
# If the sentiment is negative, send the input to the negative branch.
def is_negative(analysis: dict) -> bool:
    return analysis["sentiment"].sentiment == "negative"


# Convert the Pydantic object into plain text before sending it to reply prompts.
def normalize_for_reply(analysis: dict) -> dict:
    return {
        "feedback": analysis["feedback"],
        "sentiment": analysis["sentiment"].sentiment,
    }


# Conditional reply chain:
# - Positive sentiment -> positive_reply_prompt -> model -> parser
# - Negative sentiment -> negative_reply_prompt -> model -> parser
response_chain = RunnableLambda(normalize_for_reply) | RunnableBranch(
    (is_negative, negative_reply_prompt | model | text_parser),
    positive_reply_prompt | model | text_parser,
)


# Full conditional chain:
# 1. analysis_chain detects sentiment and keeps feedback.
# 2. response_chain picks the correct reply path.
chain = analysis_chain | response_chain


# Small helper so we can see both branches clearly.
def run_feedback_flow(feedback: str) -> None:
    print("FEEDBACK:")
    print(feedback)

    analysis = analysis_chain.invoke({"feedback": feedback})

    print("\nSENTIMENT:")
    print(analysis["sentiment"].sentiment)

    final_reply = response_chain.invoke(analysis)

    print("\nFINAL REPLY:")
    print(final_reply)
    print("\n" + "-" * 50 + "\n")


# Example 1: positive feedback.
run_feedback_flow(
    "I love the app experience. The support team was quick and very helpful."
)


# Example 2: negative feedback.
run_feedback_flow(
    "I am upset because my issue is still not resolved and no one has replied."
)


# For visualization of the chain flow in terminal.
chain.get_graph().print_ascii()


"""
Same logic without using a conditional chain:

analysis = analysis_chain.invoke({"feedback": feedback})

if analysis["sentiment"].sentiment == "negative":
    prompt = negative_reply_prompt.invoke(analysis)
else:
    prompt = positive_reply_prompt.invoke(analysis)

final_reply = text_parser.invoke(model.invoke(prompt))

print(final_reply)

Why conditional chains are useful:
- Different sentiment needs different wording.
- Positive feedback can get a thankful response.
- Negative feedback can get an apology and escalation.
- This pattern is useful for support bots, routing, moderation,
  and many other classification-based workflows.
"""
