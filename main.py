from locale import currency
from core.callback import ErrorHandler, BaseCallback
from core.chains import rag_chain
from core.models import currency_model

text = "Кто такой Пьер?"

answer = rag_chain.invoke({"question": text, "book": "war-and-peace-2"}) #, config={"callbacks": [BaseCallback(), ErrorHandler()]}

print(answer)

