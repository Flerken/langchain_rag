from pprint import pprint
from random import choice
from langchain_core.runnables import RunnableLambda
from langchain_core.messages import AIMessage

def format_docs_func(results):
    final_docs = {}

    for result in results:
        #print(result)
        #print("#*#" * 50)
        for rank, doc in enumerate(result):
            chunk_id = doc.metadata["_id"]
            score = 1.0 / (rank + 1)

            if chunk_id not in final_docs:
                final_docs[chunk_id] = {
                    "document" : doc,
                    "score" : 0
                }

            final_docs[chunk_id]["score"] += score

    final_docs = sorted(final_docs.values(), key=lambda x: x["score"], reverse=True)[:12]

    pprint(final_docs)

    return "\n\n".join(doc["document"].page_content for doc in final_docs)

format_docs = RunnableLambda(format_docs_func)

def queries_list_func(inputs: dict):
    print(inputs)
    print("\n\n\n")
    return [{"question": i, "book": inputs["book"]} for i in inputs["queries"]]

queries_list = RunnableLambda(queries_list_func)