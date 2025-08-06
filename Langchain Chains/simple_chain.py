from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()  

prompt = PromptTemplate(
    template="Generate 5 interesting fact about {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

# | is the pipe operator used to chain components in Langchain

chain = prompt | model | parser

result = chain.invoke({"topic": "Python programming language"})

print(result)

chain.get_graph().print_ascii() # This will print the graph of the chain
# The graph shows how the components are connected and the flow of data through the chain

