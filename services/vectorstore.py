from core.config import settings
from services.embeddings import embedder, vector_size

from qdrant_client.models import Distance, VectorParams
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient


client = QdrantClient(host="localhost", port=6333)
collection_name = "war-and-peace"

if not client.collection_exists(collection_name):
    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
    )

vectorstore_q = QdrantVectorStore(client=client, collection_name=collection_name, embedding=embedder)

#first_chunk = chunks[0]

#print(first_chunk)
#print(len(first_chunk.page_content))
#
#
#
#aoi_embedder = OpenAIEmbeddings(
#    model="openai/text-embedding-3-large",
#    api_key = settings.CLOUD_API_KEY,
#    base_url = settings.CLOUD_BASE_URL,
#)
#
#vector = embedder.embed_query(first_chunk.page_content)
#aoi_vector = aoi_embedder.embed_query(first_chunk.page_content)
#
#print(aoi_vector)
#print(len(aoi_vector))

#async def main():
#    chunks = get_chunks(Path("../docs/war-and-peace-1.txt"))
#    await vectorstore_q.aadd_documents(documents=chunks)
#
#asyncio.run(main())