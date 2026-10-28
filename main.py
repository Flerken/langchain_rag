from langchain_core.messages import ToolMessage

from core.chains import currency_chain
from core.prompts import currency_prompt, tools_prompt
from core.t_models import tools_model
from tools import convert_currency_tool, iphone_price, rag, current_time
from shemas.multyquery import ToolAnswer
from langchain.agents import create_agent
from langchain.agents.structured_output import ProviderStrategy, ToolStrategy
from core.models import gigachat_model

#text = "Кто такой Пьер?"


#print(text)

text = input("Введите свой запрос: ")
result = currency_chain.invoke({"text": text})
# print(result)

tools = [
    convert_currency_tool,
    iphone_price,
    rag,
    current_time
]

tool_agent = create_agent(model=gigachat_model, tools=tools, system_prompt=tools_prompt, response_format=ToolAnswer)

result = tool_agent.invoke({"messages": currency_prompt.invoke({"text": text})})

print(result)