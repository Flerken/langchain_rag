from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.runnables import RunnableLambda


#prompt_template = ChatPromptTemplate([
#    SystemMessagePromptTemplate.from_template_file('./prompts/war-and-peace.txt', ["context", "question"]),
#    HumanMessagePromptTemplate.from_template("{text}")
#])
#
#def currency_prompt_func(input_dict: dict):
#    return prompt_template.format_messages(**input_dict)

#prompt = RunnableLambda(currency_prompt_func)

prompt = ChatPromptTemplate.from_template("""
Ответь на вопрос, использую контекст ниже.
Если ответа в контексте нет, так и скажи.

Контекст: {context}

Вопрос: {question}

Ответ:
""")
