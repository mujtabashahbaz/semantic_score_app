import streamlit as st
import requests
import json

# Function to call OpenAI API for semantic analysis using GPT-3.5 Turbo
def get_semantic_score(api_key, blog_content):
    url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    
    # Prepare the messages for the chat model
    messages = [
        {"role": "system", "content": "You are an AI that evaluates the quality of written content."},
        {"role": "user", "content": f"Evaluate the following blog post for semantic quality, relevance, cohesion, and clarity. Provide a score from 0 to 10: {blog_content}"}
    ]
    
    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages,
        "max_tokens": 200,
        "temperature": 0.7,
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        # Extracting the response
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
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
