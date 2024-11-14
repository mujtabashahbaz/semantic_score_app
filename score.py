import streamlit as st
import requests

# Function to call OpenAI API for semantic analysis
def get_semantic_score(api_key, blog_content):
    url = "https://api.openai.com/v1/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    
    data = {
        "model": "text-davinci-003",
        "prompt": f"Evaluate the following blog post for semantic quality, relevance, cohesion, and clarity. Return a score from 0 to 10: {blog_content}",
        "max_tokens": 100,
        "temperature": 0.7,
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        # Extracting the response
        result = response.json()
        # The response will have the text with the score, let's return it
        return result["choices"][0]["text"].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"

# Streamlit app layout
st.title("Blog Semantic Score Analyzer")

# Ask for the OpenAI API key
api_key = st.text_input("Enter your OpenAI API key", type="password")

# Ask for the blog content
blog_content = st.text_area("Enter the blog content here:")

if st.button("Analyze"):
    if api_key and blog_content:
        # Call the API and get the semantic score
        result = get_semantic_score(api_key, blog_content)
        st.subheader("Semantic Score Analysis")
        st.write(result)
    else:
        st.error("Please provide both API key and blog content.")
