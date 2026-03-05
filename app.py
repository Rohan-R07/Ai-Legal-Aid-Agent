import streamlit as st
import requests
import json
from rag import load_law_context
from prompt import SYSTEM_PROMPT

# --- OLLAMA API anrop ---
def get_ollama_response(prompt: str, model: str, host: str):
    """
    Calls the Ollama API at a specified host, streams the response, and handles errors.
    """
    try:
        url = f"{host}/api/generate"
        response = requests.post(
            url,
            json={"model": model, "prompt": prompt, "stream": True},
            stream=True
        )
        response.raise_for_status()

        st.subheader("Generated Response:")
        placeholder = st.empty()
        full_response = ""
        for line in response.iter_lines():
            if line:
                try:
                    json_line = json.loads(line)
                    if "response" in json_line:
                        full_response += json_line["response"]
                        placeholder.markdown(full_response)
                except json.JSONDecodeError:
                    st.error("Error decoding JSON from Ollama stream.")
                    continue
    
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            st.error(f"Model '{model}' not found at {host}. Please check the model name and host address.")
            st.info("Ensure the model is pulled and available on the Ollama server.")
        else:
            st.error(f"HTTP Error connecting to Ollama: {e}")
    except requests.exceptions.RequestException as e:
        st.error(f"Connection Error: Could not connect to {host}. Please ensure the server is running and the URL is correct.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

# --- Streamlit UI ---
st.set_page_config(layout="wide")

st.title("Legal Aid Assistant")
st.markdown("This tool provides legal information based on your issue. It is not a substitute for legal advice.")

# --- Sidebar ---
st.sidebar.header("Instructions")
st.sidebar.info(
    """
    1.  **Enter Model Name**: Make sure the model name below matches one from your `ollama list`.
    2.  **Select Issue Type**: Choose the legal area.
    3.  **Describe Your Problem**: Write a clear description.
    4.  **Get Information**: Click the button to generate a response.
    """
)

st.sidebar.header("Configuration")
ollama_host = st.sidebar.text_input("Ollama Host URL:", "http://localhost:11434")
model_name = st.sidebar.text_input("Ollama Model Name:", "qwen:0.5b")
st.sidebar.info("The default Ollama Host URL works for local execution. Change it only if you are hosting Ollama elsewhere.")
st.sidebar.info("Run `ollama list` in your terminal to see available local models on your machine.")


# --- Main Page ---
issue_type = st.selectbox(
    "Select the type of legal issue:",
    ("Consumer", "Employment", "Traffic", "Civil")
)

user_query = st.text_area(
    "Describe your legal problem here:",
    height=150,
    placeholder="For example: 'I bought a new laptop that stopped working after a week, and the store refuses to refund me.'"
)

if st.button("Get Legal Guidance"):
    if not user_query:
        st.warning("Please describe your problem in the text box.")
    elif not model_name:
        st.warning("Please enter the Ollama model name in the sidebar.")
    elif not ollama_host:
        st.warning("Please enter the Ollama Host URL in the sidebar.")
    else:
        with st.spinner(f"Analyzing your query with model '{model_name}'..."):
            legal_context = load_law_context(issue_type)
            full_prompt = f"{SYSTEM_PROMPT}\n\nContext: {legal_context}\n\nQuery: {user_query}"
            
            # Pass the host URL to the function
            get_ollama_response(full_prompt, model=model_name, host=ollama_host)
            
st.sidebar.header("About")
st.sidebar.markdown("All processing happens locally on your machine via Ollama, utilizing a local language model.")