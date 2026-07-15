"""
# Pypdf works only with text pdf and not other types of pdfs like scanned images

# Avoid using these community versions, because they are not verified by lanchain,
and langchain do endorse them, they are contributed by langchain community

"""

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('sample-local-pdf.pdf')

docs = loader.load()

print(len(docs))

print(docs[0])