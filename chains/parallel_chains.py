"""
PARALLEL CHAIN IN LANGCHAIN

Goal:
- Learn how to run multiple LLM tasks in parallel from the same input.
- Here, one document is used to generate:
  1. Notes
  2. Quiz
- Then both outputs are combined into one final answer.

Basic flow:
Document -> Parallel branches -> Combine prompt -> Model -> Parser

Meaning:
1. The same input text is sent to two different prompts at the same time.
2. One branch creates notes.
3. The other branch creates a quiz.
4. A final prompt joins both outputs together.
5. The model returns the final response.
6. The parser extracts clean text.
"""

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI


# Loads API keys and environment variables from the .env file.
load_dotenv()


# One model is enough here.
# We can reuse it in multiple branches of the parallel chain.
model = ChatOpenAI()


# Parser converts the final AIMessage into plain text.
parser = StrOutputParser()


# Branch 1: create short notes from the document.
notes_prompt = PromptTemplate(
    template="Read the following document and write short notes:\n\n{document}",
    input_variables=["document"],
)


# Branch 2: create a quiz from the same document.
quiz_prompt = PromptTemplate(
    template="Read the following document and create a short quiz with answers:\n\n{document}",
    input_variables=["document"],
)


# Combine prompt:
# This step receives both branch outputs and merges them into one response.
combine_prompt = PromptTemplate(
    template=(
        "Combine the notes and quiz into one clean answer.\n\n"
        "Notes:\n{notes}\n\nQuiz:\n{quiz}"
    ),
    input_variables=["notes", "quiz"],
)


# Parallel chain:
# The same document goes into two branches at the same time.
# Left branch -> notes
# Right branch -> quiz
# Then both are passed into the final combine prompt.
parallel_chain = RunnableParallel(
    notes=notes_prompt | model | parser,
    quiz=quiz_prompt | model | parser,
)


# Full chain:
# 1. parallel_chain creates notes and quiz in parallel.
# 2. combine_prompt merges both results.
# 3. model writes the final combined response.
# 4. parser returns the final plain string.
chain = parallel_chain | combine_prompt | model | parser


# invoke() starts the parallel step first.
# This lets us print notes and quiz separately before showing the final output.
document = "LangChain helps you build LLM applications using prompts, models, parsers, and chains."
parallel_result = parallel_chain.invoke({"document": document})


print("NOTES:")
print(parallel_result["notes"])
print("\nQUIZ:")
print(parallel_result["quiz"])


# Now combine both outputs into the final result.
combined_prompt = combine_prompt.invoke(parallel_result)
final_result = parser.invoke(model.invoke(combined_prompt))


print("\nFINAL OUTPUT:")
print(final_result)


# For visualization of the chain flow in terminal.
chain.get_graph().print_ascii()


"""
Same logic without using a parallel chain:

notes_prompt_value = notes_prompt.invoke({"document": document})
notes = parser.invoke(model.invoke(notes_prompt_value))

quiz_prompt_value = quiz_prompt.invoke({"document": document})
quiz = parser.invoke(model.invoke(quiz_prompt_value))

combined_prompt = combine_prompt.invoke({"notes": notes, "quiz": quiz})
final_result = parser.invoke(model.invoke(combined_prompt))

print(final_result)

Why parallel chains are useful:
- Multiple tasks can start from the same input.
- Independent work happens side by side.
- It is useful for tasks like notes + quiz, summary + sentiment,
  or extract + classify.
"""
