import streamlit as st
import cohere
import os
from dotenv import load_dotenv

load_dotenv()
co = cohere.Client("VKXPPqm6LR3tM1u3lpjtgyjAyrcvdeVLD9wQJNYc")
def get_cohere_blog(input_text, no_words, blog_style):
    prompt = f"""
    Write a blog for a {blog_style} job profile on the topic "{input_text}".
    The blog should be engaging, informative, and within {no_words} words.
    """
    response = co.chat(
        model="command-r-plus-08-2024",
        message=prompt,
        temperature=0.5,
    )

    return response.text.strip()
st.set_page_config(  
    page_title="Generate Blogs with Cohere 🤖",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.header("Generate Blogs with Cohere 🤖")

input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([5, 5])
with col1:
    no_words = st.text_input("Number of Words")
with col2:
    blog_style = st.selectbox(
        "Writing the blog for",
        ("Researchers", "Data Scientist", "Common People","Student"),
        index=0
    )
if st.button("Generate"):
    if input_text.strip() and no_words.strip():
        with st.spinner("Generating blog using Cohere..."):
            try:
                response = get_cohere_blog(input_text, no_words, blog_style)
                st.subheader("Generated Blog:")
                st.write(response)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter both a topic and number of words before submitting.")