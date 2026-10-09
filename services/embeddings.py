from core.config import settings

from langchain_gigachat.embeddings import GigaChatEmbeddings
from langchain_openai.embeddings import OpenAIEmbeddings

#embedder = GigaChatEmbeddings(
#    credentials=settings.GIGACHAT_CREDENTIALS,  # замени на свой
#    verify_ssl_certs=False,
#    scope="GIGACHAT_API_PERS",
#    max_retries=3,
#    retry_backoff_factor=0.5
#)
#aoi_embedder = OpenAIEmbeddings(
#    model="openai/text-embedding-3-large",
#    api_key = settings.CLOUD_API_KEY,
#    base_url = settings.CLOUD_BASE_URL,
#)
embedder = OpenAIEmbeddings(
    model="Qwen/Qwen3-Embedding-0.6B",
    api_key = settings.CLOUD_API_KEY,
    base_url = settings.CLOUD_BASE_URL,
)

vector_size = len(embedder.embed_query("Пример"))

#aoi_embedder = OpenAIEmbeddings(
#    model="openai/text-embedding-3-large",
#    api_key = settings.CLOUD_API_KEY,
#    base_url = settings.CLOUD_BASE_URL,
#)
