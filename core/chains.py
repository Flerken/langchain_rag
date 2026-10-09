from langchain_core.runnables import Runnable, RunnableLambda, RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import MarkdownListOutputParser, StrOutputParser

from rag.retriver import base_retriever, book_retriever
from core.prompts import prompt, multi_query_prompt
from core.parsers import format_docs, queries_list
from core.models import currency_model, currency_model_fallback, queries_generator_model


queries_chain = RunnableParallel(
    queries = multi_query_prompt | queries_generator_model | RunnableLambda(lambda a: a.queries),
    book=RunnableLambda(lambda q: q["book"])
) | queries_list

rag_chain = (
    RunnableParallel(
        queries = queries_chain,
        question=RunnableLambda(lambda q: q["question"]),
        book=RunnableLambda(lambda q: q["book"])
    )
    | RunnableParallel ({
        "context" : RunnableLambda(lambda x: x["queries"]) | book_retriever.map() | format_docs,
        "question" : RunnableLambda(lambda q: q["question"]),
        "book" : RunnableLambda(lambda q: q["book"])
    })
    | prompt
    | currency_model
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