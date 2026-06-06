# RAG-Chatbot
Chat with your PDF documents using RAG — LangChain, FAISS/ChromaDB, HuggingFace, Streamlit &amp; FastAPI
# RAG PDF Assistant

A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their content using LangChain, FAISS, Hugging Face, and Streamlit.

## Features

* PDF Upload
* Document Chunking
* Semantic Search using Embeddings
* FAISS Vector Database
* Context-Aware Question Answering
* Streamlit User Interface

## Tech Stack

* Python
* LangChain
* Hugging Face
* FAISS
* Streamlit
* PyPDF

## Project Architecture

PDF Upload → Document Loader → Text Chunking → Embeddings → FAISS Vector Store → Retriever → LLM → Answer

## Installation

```bash
git clone <repository-url>
cd rag-pdf-assistant
pip install -r requirements.txt
```

Create a `.env` file:

```env
HUGGINGFACEHUB_ACCESS_TOKEN=your_token
```

Run:

```bash
streamlit run app.py
```

## Future Improvements

* Multiple PDF support
* Chat history
* Source citations (show page number)
* Conversational memory
* Modern LangChain create_retrieval_chain
* Download chat as PDF
* Dark/light theme
* ChromaDB option

```
```
