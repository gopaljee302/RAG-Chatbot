# src/rag_chain.py

from huggingface_hub import InferenceClient

from src.config import HF_TOKEN
from src.vector_store import load_vector_store


# Create HF client
client = InferenceClient(
    provider="hf-inference",
    token=HF_TOKEN
)


def ask_question(question):
    """
    Retrieve relevant chunks from FAISS
    and ask the LLM using retrieved context.
    """

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
You are a helpful assistant.

Answer ONLY from the provided context.

If the answer is not present in the context,
reply exactly:

Answer not found in the document.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat_completion(
        model="google/gemma-2-2b-it",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=512,
        temperature=0.1
    )

    return response.choices[0].message.content