# Импортируем модель GigaChat из библиотеки LangChain для отправки и получения сообщений через API GigaChat

from langchain_openai.chat_models import ChatOpenAI
from core.config import settings
from tools import convert_currency_tool, iphone_price, rag


yandex_model = ChatOpenAI(
    model=settings.OPEN_AI_CHAT_MODEL,
    api_key = settings.OPEN_AI_API_KEY,
    base_url = settings.OPEN_AI_BASE_URL,
    temperature=settings.OPEN_AI_TEMPERATURE,  # Креативность ответов
    max_tokens=settings.GIGACHAT_MAX_TOKENS,
)

tools_model = yandex_model.bind_tools([convert_currency_tool, iphone_price, rag])
