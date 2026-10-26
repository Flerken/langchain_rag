from locale import currency
from core.callback import ErrorHandler, BaseCallback
from core.chains import rag_chain
from core.models import currency_model

text = "Кто сказал фразу: Рана не здесь, а вот где"

answer = rag_chain.invoke({"question": text, "book": None}) #, config={"callbacks": [BaseCallback(), ErrorHandler()]}

print(answer)

