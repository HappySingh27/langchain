
"""
Check & verify if this has been moved out of experiment package
"""

from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings

# 1. Initialize an embedding model to analyze text meaning
embeddings = OpenAIEmbeddings()

# 2. Configure the Semantic Chunker
text_splitter = SemanticChunker(
    embeddings=embeddings,
    # other types like standard deviations are also available
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=95
)

# 3. Text extracted from your attached image
document_text = """
    "Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. "
    "The sun was bright, and the air smelled of earth and fresh grass. "
    "The Indian Premier League (IPL) is the biggest cricket league in the world. "
    "People all over the world watch the matches and cheer for their favourite teams."

    Terrorism is a big danger to peace and safety. It causes harm to people and 
    creates fear in cities and villages. When such attacks happen, they leave 
    behind pain and sadness. To fight terrorism, we need strong laws, alert 
    security forces, and support from people who care about peace and safety.
"""

# 4. Generate contextually continuous chunks
chunks = text_splitter.split_text(document_text)

for i, chunk in enumerate(chunks):
    print(f"--- Topic Chunk {i+1} ---")
    print(chunk)
