import os
import streamlit as st

from src.pdf_loader import load_pdf
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.rag_chain import ask_question


UPLOAD_DIR = "data/uploaded_pdfs"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

os.makedirs(
    "vectorstore",
    exist_ok=True
)

st.set_page_config(
    page_title="RAG PDF Assistant",
    page_icon="📄"
)

st.title("📄 RAG PDF Assistant")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    pdf_path = os.path.join(
        UPLOAD_DIR,
        uploaded_file.name
    )

    with open(pdf_path, "wb") as f:
        f.write(
            uploaded_file.getbuffer()
        )

    with st.spinner(
        "Processing PDF..."
    ):

        docs = load_pdf(pdf_path)

        chunks = split_documents(
            docs
        )

        create_vector_store(
            chunks
        )

    st.success(
        "PDF processed successfully!"
    )

question = st.text_input(
    "Ask a question about the PDF"
)

if st.button("Ask"):

    if question:

        with st.spinner(
            "Generating answer..."
        ):

            answer = ask_question(
                question
            )

        st.subheader(
            "Answer"
        )

        st.write(answer)