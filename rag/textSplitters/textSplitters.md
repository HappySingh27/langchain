"""
Text Splitting :
    - Text Splitting is the process of breaking large chunks of text (like articles,
    PDFs, HTML pages or books) into smaller, manageable pieces (chunks) that an LLM
    can handle effectively.

Overcoming model limitations :
    - Many embedding models and language models have maximum input size constraints.
    Splitting allows us to process documents that would otherwise exceeds these limits.

Downstream tasks :
    - Text splitting improves nearly every LLM powered task
        - Embedding : short chunks yields more accurate vectors
        - Semantic Search : searched results point to focused info, not noise
        - Summarization : prevents hallucination and topic drift

Optimizing computational resources :
    - working with smaller chunks of text can be more memory-efficient and allow for 
    better parallelization of processing tasks.

Some Text Splitters types :-
 1. Length Based : based on length of chunks
        - length can be based on characters or chunks
        - https://www.chunkviz.com/ - website to check how your text would be splitted 
        to chunks
        - it is fast but semantic meaning is lost sometimes because chunks are based on
        length and not as per para or meaning.
 2. Text Structure Based
 3. Document Structure Based
 4. Semantic meaning based

"""