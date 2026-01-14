import os
import streamlit as st

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama

from utils import process_pdfs

st.set_page_config(
    page_title="Resume RAG Chatbot (Ollama)",
    layout="wide"
)

st.title("📄 Resume Search Chatbot (Fully Local – Ollama)")

# ---------------- PDF Upload ----------------
uploaded_files = st.file_uploader(
    "Upload bulk resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    with st.spinner("Indexing resumes..."):
        process_pdfs(uploaded_files)
    st.success("✅ Resumes indexed successfully")

# ---------------- Load Vector Store ----------------
if os.path.exists("vectorstore"):
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    vectorstore = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    llm = Ollama(
        model="llama3",
        temperature=0
    )

    # ✅ QUERY MUST BE DEFINED FIRST
    query = st.text_input("Ask about candidates:")

    # ✅ THEN CHECK IT
    if query:
        with st.spinner("Searching resumes..."):

            docs = retriever.invoke(query)

            context = "\n\n".join(doc.page_content for doc in docs)

            prompt = f"""
You are an HR resume screening assistant.

Answer ONLY using the resume data below.
If the information is not present, say "Not found in resumes".

RESUME DATA:
{context}

QUESTION:
{query}
"""

            answer = llm.invoke(prompt)

        st.subheader("🧑‍💼 Answer")
        st.write(answer)

        st.subheader("📂 Matched Resume Sections")
        for i, doc in enumerate(docs, 1):
            st.markdown(f"**Match {i}**")
            st.write(doc.page_content)
            st.markdown("---")
