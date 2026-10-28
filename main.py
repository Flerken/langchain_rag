from langchain_core.messages import ToolMessage

from core.chains import currency_chain
from core.prompts import currency_prompt, tools_prompt
from core.t_models import tools_model
from tools import convert_currency_tool, iphone_price, rag
from langchain.agents import create_agent
from core.models import gigachat_model

#text = "Кто такой Пьер?"


#print(text)

text = input("Введите свой запрос: ")
result = currency_chain.invoke({"text": text})
# print(result)

tools = [
    convert_currency_tool,
    iphone_price,
    rag
]

tool_agent = create_agent(model=gigachat_model, tools=tools, system_prompt=tools_prompt)

result = tool_agent.invoke({"messages": currency_prompt.invoke({"text": text})})

print(result)