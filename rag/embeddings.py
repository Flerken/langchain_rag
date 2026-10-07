from pathlib import Path
from core.config import settings
import asyncio
from rag.splitter import get_chunks

from langchain_ollama import OllamaEmbeddings
from langchain_gigachat.embeddings import GigaChatEmbeddings
from langchain_openai.embeddings import OpenAIEmbeddings
from qdrant_client.models import Distance, VectorParams
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient


chunks = get_chunks(Path("../docs/war-and-peace-1.txt"))

first_chunk = chunks[0]

print(first_chunk)
print(len(first_chunk.page_content))

embedder = GigaChatEmbeddings(
    credentials=settings.GIGACHAT_CREDENTIALS,  # замени на свой
    verify_ssl_certs=False,
    scope="GIGACHAT_API_PERS"
)

aoi_embedder = OpenAIEmbeddings(
    model="openai/text-embedding-3-large",
    api_key = settings.CLOUD_API_KEY,
    base_url = settings.CLOUD_BASE_URL,
)

vector = embedder.embed_query(first_chunk.page_content)
aoi_vector = aoi_embedder.embed_query(first_chunk.page_content)

print(aoi_vector)
print(len(aoi_vector))