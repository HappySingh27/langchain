from langchain_text_splitters import CharacterTextSplitter

# 1. Sample text to split
text = """[Verse 1]
I am looking in the mirror and I see a giant. 
Every step I take is shaking up the whole environment. 
Got the bass turned up, making history tonight. 
Big dreams, big steps, living under neon light.

[Chorus]
Big me, big me, ruling over the town. 
Little world around me, I will never look down. 
Big me, big me, feel the rhythm and pace. 
Little big explosion taking over the space.

[Verse 2]
Tiny voices in the crowd try to tell me what to do. 
But I am looking at the sky and my vision is true. 
Got the synth lines pumping, running through my veins. 
Breaking all the boundaries, breaking all the chains.

[Outro]
Little big, big me, louder than the thunder. 
Leaving everyone behind in absolute wonder. 
Turn it up, spin it back, let the record play. 
Big me is here, and I am here to stay."""


# 2. Initialize the splitter
splitter = CharacterTextSplitter(
    separator="\n\n",   # The exact character sequence to split on
    chunk_size=40,      # Maximum character count per chunk
    chunk_overlap=10    # Overlapping characters between adjacent chunks, 10% to 20% is a good overlap for RAG based applications
)

"""
CharacterTextSplitter 
    - splits text ONLY at the exact literal string specified 
in the `separator` parameter (like "\n\n"). It prioritizes this separator 
over your `chunk_size` limit. If a paragraph lacks the separator, the splitter 
refuses to cut mid-text, keeping the entire block intact and throwing a size 
warning because the resulting chunk drastically exceeds your target limit.

RecursiveCharacterTextSplitter 
    - fixes this by using a prioritized list of 
fallback separators: paragraphs ("\n\n"), lines ("\n"), and spaces (" "). 
It prioritizes your `chunk_size` limit; if a paragraph is too large, it 
automatically drops down to split by lines or words. This keeps your chunk 
sizes consistent and optimized for LLMs without cutting words in half.
    - RecursiveCharacterTextSplitter can be used for splitting text in file which
is not normal text like markdown file, code fiels : .py, .java or .sql to achieve
same use different set of seprators like \nclass, \ndef etc.
"""

# 3. Create plain text chunks
chunks = splitter.split_text(text)
print("Plain text chunks:", chunks)

# 4. Alternatively, create LangChain Document objects (retains metadata)
docs = splitter.create_documents([text])
print("Document object:", docs[0].page_content)

"""
Todo : 
    - here you can load text using text loader & then pass it to text splitter for splitting
    splitter.split_documents() can be used
"""
