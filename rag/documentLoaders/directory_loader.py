"""
1. Directory Loader ;
    - Directory loader is a document loader that lets you load
      multiple documents from a directory of files.

Example:
    from langchain_community.document_loaders.directory import DirectoryLoader

    loader = DirectoryLoader("./data")
    docs = loader.load()
    print(len(docs))
    print(docs[0].page_content[:300])

Notes:
    - `DirectoryLoader.load()` returns a list of Document objects.
    - `DirectoryLoader.lazy_load()` yields Document objects one at a time.
    - `glob` controls which files to match, e.g. "*.txt".
    - `recursive=True` searches subdirectories.
    - `exclude=["*.py"]` skips matching files.
    - `loader_cls` lets you choose which parser to use for each file.
    - `loader_kwargs` are passed to the inner file loader.

This file also includes a runnable demo that creates a small `example_data`
folder and loads `.txt` files from it.

2. load() vs lazy_load()

"""

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# loads all data at once in memory
docs = loader.load()

# loads in chuncks
# docs = loader.lazy_load()

print(len(docs))
print(len(docs[0].page_content))
print(len(docs[0].metadata))