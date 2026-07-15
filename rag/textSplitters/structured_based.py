from langchain_text_splitters import Language, RecursiveCharacterTextSplitter

# 1. Sample Python code string to split
python_code = """
class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_all(self):
        # High priority operational logic
        results = []
        for item in self.data:
            cleaned = item.strip().lower()
            results.append(cleaned)
        return results

def helper_function():
    print("System execution completed successfully.")
"""

# 2. Initialize the splitter optimized for Python structure
# It automatically targets structural tokens: class -> def -> if/for -> spaces
code_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, 
    chunk_size=100, 
    chunk_overlap=30
)

# 3. Split the code syntax cleanly
code_chunks = code_splitter.split_text(python_code)

# 4. Display the structurally separated chunks
for i, chunk in enumerate(code_chunks):
    print(f"--- Code Chunk {i+1} ---")
    print(chunk)
