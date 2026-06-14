#static prompt :
"""A static prompt is a fixed instruction given to an AI model that remains exactly the same every time you use it. 
    Unlike dynamic prompts that adjust based on user input, static prompts are rigid and do not change unless you manually edit"""


from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

model = ChatOpenAI(model='gpt-4',temperature=1.5,max_completion_tokens=50)

st.header('Research Tool')

#user_input = st.text_input('Enter your prompt') static prompt replaced with dyanmic prompt below

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need",
"BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners",
"Diffusion Models Beat GANs on Image Synthesis" ] )

style_input = st.selectbox( "Selecty Explanation Style", ["Beginner-Friendly", "Technical","Code-Oriented", "Mathematical"])

length_input = st. selectbox ("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium(3-5 paragraphs) ",
                                                            "Long (detailed explanation)"])


template = load_prompt('template.json')

#invoke the variable in template
prompt = template.invoke({'paper_input':paper_input,
                 'style_input':style_input,
                 'length_input':length_input})

if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result.content)
