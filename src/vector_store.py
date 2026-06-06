from langchain_community.vectorstores import FAISS

from src.embeddings import get_embeddings

INDEX_PATH = "vectorstore/faiss_index"


def create_vector_store(chunks):

    embeddings = get_embeddings()

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    vector_store.save_local(INDEX_PATH)

    return vector_store


def load_vector_store():

    embeddings = get_embeddings()

    return FAISS.load_local(
        INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )