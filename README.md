# ⚖️ Legal AI Assistant

An AI-powered legal assistant that helps users understand **real-world legal problems** using natural language.
The system simplifies complex legal concepts and provides guidance across **employment, consumer, and civil/traffic law scenarios**.

This project demonstrates how **Local Large Language Models (LLMs)** can be used to build a practical legal assistance tool that runs with minimal external dependencies.

---

# 🚀 Key Features

* AI-powered legal question answering
* Covers multiple real-world legal domains
* Simplifies complex legal topics
* Provides scenario-based legal guidance
* Runs using **local LLMs for privacy and speed**

---

# 📂 Legal Domains Covered

The assistant focuses on common legal issues faced by people in everyday life.

## 1️⃣ Employment Law

Helps users understand workplace rights and employer responsibilities.

Example prompts:

* My employer has not paid my salary for two months. What legal action can I take?
* My company terminated me without notice. Is that legal?
* I am facing harassment at work and HR is not responding. What are my options?

---

## 2️⃣ Consumer Law

Provides guidance on product, service, and marketplace disputes.

Example prompts:

* I bought a laptop online but it stopped working in two days. What can I do?
* The seller refused to replace a defective product. What are my rights?
* I paid for an online service but the company never delivered it. How can I file a complaint?

---

## 3️⃣ Civil & Traffic Law

Assists with disputes and common legal problems.

Example prompts:

* My landlord is refusing to return my security deposit. What can I do legally?
* I received a traffic challan but I believe it was issued incorrectly. How can I challenge it?
* I was involved in a minor road accident. What legal steps should I take?

---

# 🎥 Full Demo

Example interaction with the assistant.

User Prompt:

My employer has not paid my salary for two months. What legal action can I take?

AI Response:

The assistant explains possible employee rights, relevant labor protections, and potential legal actions such as filing a complaint with the labor department or seeking legal assistance.

---

# 🧠 AI Architecture

The application processes legal queries using a **local language model pipeline**.

Workflow:

User Input
↓
Prompt Processing
↓
Local LLM via Ollama
↓
AI Generated Response
↓
Displayed to User

This approach enables natural language legal assistance while keeping model inference local.

---

# 🤖 Local LLM

This project runs on a **Local Large Language Model (LLM)** instead of relying on external APIs.

### Model Used

**Qwen 2.5B**

Reasons for choosing this model:

* Lightweight and efficient
* Good reasoning capability for small models
* Suitable for running locally
* Faster inference on standard hardware

---

# ⚙️ Backend AI Engine

The project uses **Ollama** to run the language model locally.

Ollama allows developers to easily run and manage LLMs on their machine without complex setup.

Advantages:

* Local inference
* Faster response time
* No external API dependency
* Better data privacy

---

# 🛠️ Tech Stack

Frontend

* Application Interface

Backend

* Prompt processing layer

AI Engine

* Ollama

Language Model

* qwen2.5:1.5b (Local LLM)

---

# 🧑‍💻 Installation & Setup

Follow the steps below to run the project locally.

## 1️⃣ Install Ollama

Download and install Ollama from the official website:

https://ollama.com

Verify installation:

```bash
ollama --version
```

---

## 2️⃣ Pull the Language Model

Download the **Qwen 2.5B model** using Ollama:

```bash
ollama pull qwen2.5:1.5b
```

or

```bash
ollama pull qwen2.5:1.5b
```

*(Choose based on your system capability.)*

---

## 3️⃣ Run the Model

Start the model locally:

```bash
ollama run qwen2.5:1.5b
```

Ollama will now serve the model locally.

---

## 4️⃣ Run the Application

Clone the repository:

```bash
git clone https://github.com/yourusername/legal-ai-assistant.git
```

Navigate into the project folder:

```bash
cd legal-ai-assistant
```

Run the application according to your environment.

---

# 💡 Example Queries

You can test the system using prompts like:

Employment

* My employer has not paid my salary for two months. What should I do?

Consumer

* The seller refused to replace a defective product. What are my rights?

Civil

* My landlord is refusing to return my security deposit.

Traffic

* I received a traffic challan that I believe is incorrect.

---

# 📈 Future Improvements

* Legal document summarization
* Contract analysis
* Case law referencing
* Multi-language support
* Voice-based legal queries

---

# ⚠️ Disclaimer

This project provides **general legal information for educational purposes only** and should not be considered professional legal advice.

Always consult a qualified legal professional for official guidance.

---

# 📜 License

This project is licensed under the **Apache License 2.0**.

See the full license in the repository:
[LICENSE](./LICENSE)
