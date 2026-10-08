from langchain_core.runnables import Runnable, RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import MarkdownListOutputParser, StrOutputParser

from rag.retriver import base_retriever, book_retriever
from core.prompts import prompt
from core.parsers import format_docs
from core.models import currency_model, currency_model_fallback


rag_chain = ({
    "context" : book_retriever | format_docs,
    "question" : RunnableLambda(lambda q: q["question"])
    }
    | prompt
    | currency_model_fallback
    | StrOutputParser()
)

#dishes_chain = dishes_chain.with_fallbacks(
#    fallbacks=[emergency_dishes_chain],
#    exceptions_to_handle=[Exception]
#)
#
#recipe_chain = (chef_prompt | recipe_model | make_markdown)
#
#
#super_chain = dishes_chain | random_dish | dish_to_dict | recipe_chain