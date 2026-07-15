"""

# Pypdf works only with text pdf and not other types of pdfs like scanned images

# Avoid using these community versions, because they are not verified by lanchain,
and langchain do endorse them, they are contributed by langchain community

from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader('sample-local-pdf.pdf')
docs = loader.load()
print(len(docs))
print(docs[0])

# Docling : 
     - Docling is an open-source document processing library that converts documents 
	   (PDFs, Word files, PowerPoint, HTML, images, etc.) into structured, 
	   machine-readable data that is optimized for AI and RAG applications.
	   Internally it uses HF models to understand the loaded docs
"""

from dotenv import load_dotenv
import os

load_dotenv()

# quick check whether HF token is visible to this Python process
hf_token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACEHUB_API_TOKEN")
if hf_token:
	print("HF token detected in environment.")
else:
	print("HF token not found; you may see unauthenticated HF Hub warnings.")

# ensure the token is available under common env var names used by HF libraries
if hf_token:
	for name in ("HF_TOKEN", "HUGGINGFACEHUB_API_TOKEN", "HF_HUB_TOKEN"):
		os.environ[name] = hf_token
	# try to programmatically register the token with huggingface_hub (safe no-op if not installed)
	try:
		from huggingface_hub import login

		try:
			login(token=hf_token, add_to_git_credential=False)
		except TypeError:
			# older/newer versions may have different signature; ignore failures
			pass
	except Exception:
		pass

from langchain_docling.loader import DoclingLoader

loader = DoclingLoader('sample-local-pdf.pdf')

docs = loader.load()

print(len(docs))
