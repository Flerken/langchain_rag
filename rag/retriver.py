from core.config import settings
from services.vectorstore import vectorstore_q

retriever = vectorstore_q.as_retriever(search_type="mmr", search_kwargs={"k": 6})