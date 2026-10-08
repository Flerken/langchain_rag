from locale import currency
from core.callback import ErrorHandler, BaseCallback
from core.chains import rag_chain
from core.models import currency_model

text = "Сколько лет было графине"

answer = rag_chain.invoke(text) #, config={"callbacks": [BaseCallback(), ErrorHandler()]}

print(answer)

