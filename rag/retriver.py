from core.config import settings
from services.vectorstore import vectorstore_q

retriever = vectorstore_q.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 6,
        "fetch_k": 24,
        "lambda_mult": 1.0,
        "filter" : {
            "must": [
                {
                    "key": "metadata.Книга",
                    "match": {
                        "value": "war-and-peace-2"
                    }
                }
            ]
        }
    })