from locale import currency
from core.callback import ErrorHandler, BaseCallback
from core.chains import rag_chain
from core.models import currency_model

text = "Опиши внешний вид жены Болконского"

answer = rag_chain.invoke({"question": text, "book": "war-and-peace-1"}) #, config={"callbacks": [BaseCallback(), ErrorHandler()]}

print(answer)

