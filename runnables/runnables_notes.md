# Runnables in LangChain

These notes are written for a first-time learner and focus on the ideas behind
LangChain runnables in a clean, practical way.

## Big Picture

LangChain started with the idea of helping people build LLM-based applications more easily.
At first, the core idea was simple:

- take a prompt
- send it to an LLM
- get a response

But real applications are not that small. In practice, an LLM app may also need:

- document loading
- text splitting
- embeddings
- vector stores
- retrievers
- output parsers
- memory
- routing
- multi-step workflows

That is why LangChain evolved from simple chain-style usage into a more standard and flexible system.

## Why Chains Were Important

Before runnables, chains were the main way to connect components.
You can think of chains as a pipeline of steps, like Lego blocks.

Examples of chain styles:

- `LLMChain`
- `SequentialChain`
- `SimpleSequentialChain`
- `ConversationalRetrievalChain`
- `RetrievalQA`
- `RouterChain`
- `MultiPromptChain`
- `HydeChain`
- `AgentExecutorChain`
- `SQLDatabaseChain`

These are not random names.
Each one solved a different use case.

## Why LangChain Needed More Than Just Chains

The story starts with the history:

- ChatGPT launched in 2022
- OpenAI APIs became public
- many companies began offering LLM APIs
- developers started building LLM apps everywhere

LangChain saw that LLM apps would become common, but the real work would be bigger than “prompt in, answer out”.
For example, in a PDF reader, you may need to:

1. load the document
2. split it into chunks
3. create embeddings
4. store them in a vector database
5. retrieve relevant chunks
6. send the best chunks to the LLM
7. parse the output for the user

So LangChain started building helper components for the whole workflow, not just for the LLM call.

## The Problem With Old Chain Style

The main pain point was this:

- too many chain types
- too many separate components
- many manual steps
- different classes had different behavior
- code felt repetitive and sometimes messy

There was also a deeper problem: the chain APIs were not standardized enough.
Different chains were created for different workflows, and each new use case often
needed a new special chain. That made the learning curve steeper for beginners.

Old-style chains usually looked like specialized classes wired together for one
workflow, for example:

- `PromptTemplate`
- `LLMChain`
- `chain.run(...)` or `chain.predict(...)`

For multi-step tasks, developers used different chain classes like sequential or
router-style chains and had to learn the behavior of each one separately. Instead
of one standard contract, LangChain had many chain types with different method
names and different integration patterns.

This created three problems:

- more code to glue components together manually
- a steeper learning curve because every chain felt different
- harder composition when a new workflow needed a new special chain

Runnables solved this by giving prompts, models, parsers, and chains the same
common interface. Once everything supports `invoke()`, components can be joined
with the same pipe style and reused more easily across workflows.

For a simple app, you had to do this manually:

1. create a prompt template
2. format it
3. send it to the LLM
4. take the response
5. pass it somewhere else

That works, but it becomes annoying when applications get larger.

The big idea was:

what if LangChain could standardize the common behavior so developers did not
have to learn a different pattern for every workflow?

## What Runnables Are

Runnables are the standard interface behind LangChain workflows.

In simple words:

- a runnable is anything that can be “run”
- it accepts input
- it produces output
- it can be connected with other runnables

This is why runnables feel like a universal connector.
Once everything follows the same interface, you can connect many parts together easily.

The important shift is:

- old world: “this class has its own way of working”
- runnable world: “everything follows the same runnable contract”

This is similar to a Java interface:

- the method names stay consistent
- the implementation may differ
- integration becomes easier because every class promises the same contract

## Why Runnables Exist

Runnables exist because LangChain needed a foundation that could support:

- different model providers
- many task types
- simple chains
- long pipelines
- nested chains
- parallel execution
- conditional routing

In other words, LangChain needed one common base idea that could cover many
workflows without making every workflow a special one-off class.

## The Core Mental Model

Think of an LLM app like a pipeline:

`input -> component -> component -> component -> output`

Each component can be:

- a prompt
- an LLM
- a parser
- a retriever
- a custom function
- a full chain itself

Because chains are built from runnables, chains can also be treated as runnables.
That is the nested Lego-block idea from the lecture.

## Simple Chain Example From the Lecture Flow

A very simple example looks like this:

- prompt template
- LLM
- output

The manual version looks like this:

1. create a prompt template
2. format the prompt
3. send it to the model
4. get the answer

With chains, that becomes one connected pipeline.

That is the first win: less manual glue code.

## Bigger Chain Example

Runnables matter even more for complex flows.

Example idea:

1. one chain generates a joke
2. another chain explains the joke
3. then both chains are connected into one bigger chain

This is the key breakthrough:

- a chain can itself be treated like a runnable
- so a chain can become input to another chain

That is how LangChain supports nested workflows.

## Why the `invoke` Method Matters

`invoke` is the standard way to run a runnable.

Old methods like `run` or `predict` existed in earlier styles, but `invoke` became the cleaner standard.

Basic idea:

- `invoke()` runs one input through the runnable
- it returns the output for that input

Runnable-style APIs make things more consistent across different components.

## Other Useful Runnable Ideas

Standardization makes many patterns easier:

- sequential workflows
- parallel workflows
- conditional routing
- composition of multiple chains

That is why runnables are such a big deal.
They are not just a new feature.
They are the foundation that makes the rest of LangChain feel uniform.

## Why the Abstract Base Class Matters

The internal design idea is:

- LangChain’s core classes inherit from a runnable base
- `invoke` is defined as part of that contract
- child classes must implement the behavior

This is a software design move:

- the framework defines the interface
- concrete classes fill in the actual behavior

That is what makes the whole system consistent.

## What Changed for Developers

Runnables made LangChain easier to use because now developers can:

- connect components with a common interface
- build long pipelines
- reuse pieces in different places
- compose chains from other chains
- reduce custom glue code

So instead of thinking, “How do I wire these unrelated classes together?” you can think, “What is the flow of data?”

## Final Mental Shortcut

If you remember only one thing, remember this:

- chains are workflows
- runnables are the standardized building blocks behind those workflows
- `invoke` is the common way to run them

That is why chains became much more powerful once LangChain introduced runnables.

## One-Line Summary

Runnables are LangChain’s standard interface for building, connecting, and reusing LLM workflow components in a clean and consistent way.
