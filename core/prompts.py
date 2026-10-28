from langchain_core.messages import SystemMessage
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
Для каждого аргумента приводи источник
Если ответа в контексте нет, так и скажи.

# Контекст: {context}

# Вопрос: {question}

# Ответ:
""")

multi_query_prompt = ChatPromptTemplate.from_template("""
    Ты AI-ассистент, который помогает улучшить поиск в векторной базе данных.
    
    Твоя задача: сгенерировать 2 разных версий вопроса пользователя, чтобы найти релевантные документы в базе знаний.
    
    Оригинальный запрос: {question}
    
    Правила генерации:
        1. Сохраняй исходный смысл
        2. Используй разные формулировки и синонимы
        3. Варьируй длину: от коротких до развернутых
        4. Применяй профессиональную и бытовую лексику
        5. Не придумывай новые факты, только перефразируй
    
    Сформируй список из 2 запросов
""")

tools_prompt = SystemMessage("""
    Ты — ассистент, который помогает пользователю с разными делами: поиск товаров, расчет стоимости, конвертация валюты и тд.

    Правила использования инструментов:
    - Если ни один из инструментов не подходит, то используй common_question.
    - У тебя есть доступ к разным инструментам, если задачу пользователя можно решить с помощью инструмента, то воспользуйся.
    - Если для решения задания пользователя требуется несколько инструментов - используй несколько.
    - Используй инструменты ТОЛЬКО если они на 100% подходят.
    - Если инструмент вернул ошибку, объясни пользователю, что что-то не получилось, и предложи уточнить запрос.

    Результат возвращай в виде понятного и естественного предложения на языке пользователя в поле answer.
    Также добавь текущую дату и время в поле answer_date в понятном виде на языке пользователя.
    """)

currency_prompt_template = ChatPromptTemplate([
    HumanMessagePromptTemplate.from_template("{text}")
])


def currency_prompt_func(input_dict: dict):
    return currency_prompt_template.format_messages(**input_dict)


currency_prompt = RunnableLambda(currency_prompt_func)