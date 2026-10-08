from random import choice
from langchain_core.runnables import RunnableLambda
from langchain_core.messages import AIMessage
from shemas.choice import GeneratedMenu, GeneratedRecipe

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

format_docs = RunnableLambda(format_docs)