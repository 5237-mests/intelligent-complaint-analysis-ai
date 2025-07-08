import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import openai
import os

# Load ChromaDB vector store
chroma_client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="vector_store/chroma_db"
))
collection = chroma_client.get_collection("complaint_chunks")

# Load embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Set your OpenAI key (best practice: use environment variable)
openai.api_key = os.getenv('OPENAI_API_KEY')

def retrieve_chunks(question, k=5):
    question_embedding = embedding_model.encode([question])[0]
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=k,
        include=['documents', 'metadatas']
    )
    return results['documents'][0], results['metadatas'][0]

def build_prompt(context, question):
    return f"""
You are a financial analyst assistant for CrediTrust. Use the following context to answer the question.

Context:
{context}

Question: {question}

Answer:
"""

def generate_answer(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful financial assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.3
    )
    return response['choices'][0]['message']['content'].strip()

def rag_pipeline(question, k=5):
    chunks, metadata = retrieve_chunks(question, k)
    context = "\n\n".join(chunks)
    prompt = build_prompt(context, question)
    answer = generate_answer(prompt)
    return answer, chunks, metadata
