📄 Resume RAG Chatbot (Fully Local with Ollama)

A Retrieval-Augmented Generation (RAG) chatbot built using Streamlit, LangChain, FAISS, and Ollama that allows users to upload bulk resume PDFs and ask natural-language questions to retrieve specific candidate information.

This project runs 100% locally — no API keys, no cloud dependency, no usage limits.

1 Features

1. Upload single or multiple resume PDFs

2.Semantic search across resumes

3. Intelligent question answering using RAG

4. Fully offline & local

5. Fast retrieval using FAISS

6. No API keys, no quotas

7. Ideal for HR, recruitment, and resume screening

2 Architecture (RAG Pipeline)
PDF Resumes
   ↓
Ollama Embeddings (nomic-embed-text)
   ↓
FAISS Vector Database
   ↓
Retriever
   ↓
Ollama LLM (llama3 / mistral)
   ↓
Answer

3 Tech Stack

1.Streamlit – Web UI

2.LangChain Community – RAG utilities

3.FAISS – Vector database

4.Ollama – Local LLM & embeddings

5.PyPDF – PDF text extraction

5 Project Structure
RAG Chatbot/
│
├── app.py              # Streamlit application
├── utils.py            # PDF processing & embeddings
├── requirements.txt    # Dependencies
└── vectorstore/        # FAISS index (auto-generated)

6 Prerequisites

1️ Python
Python 3.10 or 3.11 (recommended)

2 Install Ollama
Download and install Ollama from:
 https://ollama.com/download
 Verify installation:
ollama --version

3.Pull Required Models

Run these commands in Command Prompt / Terminal (not inside Python):

ollama pull nomic-embed-text
ollama pull llama3
Check models:
ollama list

7 Installation
1 Create Virtual Environment (Recommended)
python -m venv venv
Activate:
Windows

venv\Scripts\activate

macOS / Linux

source venv/bin/activate

2 Install Dependencies
pip install -r requirements.txt

3.Run the Application

Start Ollama (if not already running):
ollama serve


Run the Streamlit app:
streamlit run app.py

Open in browser:
http://localhost:

8.Sample Questions to Ask

1.Find CTO candidates

2.What skills does the candidate have?

3.Does the candidate have AI experience?

4.Who worked on cloud platforms?

5.Summarize the resume

6.Candidate with DevOps and Kubernetes experience

7.Who reduced infrastructure costs?

9.Example Resume Used for Testing

A high-profile CTO resume (Rahul Sharma) was used to validate:

1.Skill extraction

2.Leadership experience

3.Metrics & achievements

4.Education details

10.License

This project is open for educational and personal use.
You are free to modify and extend it.

10 Acknowledgements

1.Ollama – Local LLM & embeddings

2.LangChain Community

3.FAISS – Vector similarity search

4.Streamlit – Rapid UI development

Support

If you found this project useful, give it a ⭐ on GitHub!

