from core.config import settings

from langchain_gigachat.embeddings import GigaChatEmbeddings
from langchain_openai.embeddings import OpenAIEmbeddings

embedder = GigaChatEmbeddings(
    credentials=settings.GIGACHAT_CREDENTIALS,  # замени на свой
    verify_ssl_certs=False,
    scope="GIGACHAT_API_PERS"
)
vector_size = len(embedder.embed_query("Пример"))

#aoi_embedder = OpenAIEmbeddings(
#    model="openai/text-embedding-3-large",
#    api_key = settings.CLOUD_API_KEY,
#    base_url = settings.CLOUD_BASE_URL,
#)
