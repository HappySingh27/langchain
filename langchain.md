1. Todo
    - understand langchain library/framework structure i.e how packages are organised,
    make a mental map of same so it is easier to remember what to import from where
    during coding.
    - Types of Propting
    - Ways to save tokens

2. langchain-community has been sunset and respective package has been moved to seperate integrations
like "from langchain-community.vectorstore import chroma" so each vector store has been moved to 
seperate package for example for chroma we have langchain-chroma

3. Langchain Architecture
    - langchian-core
        - langchain
        - Standalone Packages (the new integration layer, earlier it was langchain-community)

Open Questions :-
1. langchain_chroma vs langchain-chrome, difference between _ & -
2. Why vector embedding cannot be stored in relational db or mongodb