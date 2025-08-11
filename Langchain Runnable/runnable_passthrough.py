#Runnable passthrough is a simple runnable that passes
# the input directly to the output without any processing.
# It can be useful for testing or debugging purposes.

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

passThrough = RunnablePassthrough()

print(passThrough.invoke("This is a passthrough test."))