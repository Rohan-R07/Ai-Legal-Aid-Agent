import streamlit as st
import requests
import json
from rag import load_law_context
from prompt import SYSTEM_PROMPT


# --- OLLAMA API anrop ---
def get_ollama_response(prompt: str, model: str):
    """
    Calls the Ollama API to get a response from the local LLM.
    Handles streaming response and provides specific error for 404.
    """
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt, "stream": True},
            stream=True,
        )
        response.raise_for_status()

        full_response = ""
        placeholder = st.empty()
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
        placeholder.markdown(full_response)
        return full_response

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            st.error(f"Model '{model}' not found. Please check the model name.")
            st.info(
                "How to fix this:\n1. Open your terminal.\n2. Run `ollama list` to see all available models.\n3. Copy the exact name (e.g., `llama3:latest`) and paste it into the 'Ollama Model Name' box in the sidebar."
            )
        else:
            st.error(f"HTTP Error connecting to Ollama: {e}")
        return None
    except requests.exceptions.RequestException as e:
        st.error(
            f"Connection Error: Could not connect to Ollama. Please ensure it's running. Details: {e}"
        )
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return None


# --- Streamlit UI ---
st.set_page_config(layout="wide")

st.title("Legal Aid Assistant")
st.markdown(
    "This tool provides legal information based on your issue. It is not a substitute for legal advice."
)

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
model_name = st.sidebar.text_input("Ollama Model Name:", "qwen2.5:1.5b")

st.sidebar.info(
    "Run `ollama list` in your terminal to see available models on your machine."
)


issue_type = st.selectbox(
    "Select the type of legal issue:", ("Consumer", "Employment", "Traffic", "Civil")
)

user_query = st.text_area(
    "Describe your legal problem here:",
    height=150,
    placeholder="For example: 'I bought a new laptop that stopped working after a week, and the store refuses to refund me.'",
)

if st.button("Get Legal Information"):
    if not user_query:
        st.warning("Please describe your problem in the text box.")
    elif not model_name:
        st.warning("Please enter the Ollama model name in the sidebar.")
    else:
        with st.spinner(f"Connecting to model '{model_name}'..."):
            st.subheader("Generated Response:")
            get_ollama_response(
                SYSTEM_PROMPT
                + f"\n\nContext: {load_law_context(issue_type)}\n\nQuery: {user_query}",
                model=model_name,
            )

st.sidebar.header("About")
st.sidebar.markdown("All processing happens locally on your machine via Ollama, utilizing a local language model.")
