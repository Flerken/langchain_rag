from core.config import settings
from rag.splitter import get_chunks

from langchain_gigachat.embeddings import GigaChatEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient


collection_name = "war-and-peace"
client = QdrantClient(host="localhost", port=6333)
embedder = GigaChatEmbeddings(
    credentials=settings.GIGACHAT_CREDENTIALS,  # замени на свой
    verify_ssl_certs=False,
    scope="GIGACHAT_API_PERS"
)
vectorstore_q = QdrantVectorStore(client=client, collection_name=collection_name, embedding=embedder)

retriever = vectorstore_q.as_retriever(search_type="mmr", search_kwargs={"k": 6})