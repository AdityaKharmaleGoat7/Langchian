from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a tweet for {topic}",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Generate a linkedin post for {topic}",
    input_variables=["topic"],
)

model = ChatOpenAI()
parsser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet": RunnableSequence(prompt1, model, parsser),
    "linkedin_post": RunnableSequence(prompt2, model, parsser),
})

result = parallel_chain.invoke({"topic": "AI in 2024"})
print(result)
