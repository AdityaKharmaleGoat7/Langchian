from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema import RunnableParallel


load_dotenv()  

model1 = ChatOpenAI()
model2 = ChatAnthropic(model_name='claude-3-7-sonnet-20240229')

prompt1 = PromptTemplate(
    template="Generate a short and simple notes from the following text \n {text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template="Generate a 5 short questions from the following text \n {text}",    
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}",
    input_variables=["notes", "quiz"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "notes": prompt1 | model1 | parser,
        "quiz": prompt2 | model2 | parser
    }
)

merger_chain = prompt3 | model1 | parser

chain = parallel_chain | merger_chain

text = """Artificial Intelligence (AI) is the simulation of human intelligence processes by machines
    through the use of algorithms and computer systems. AI can perform tasks such as learning, reasoning, problem-solving, perception, and language understanding. It is used in various applications including robotics, natural language processing, and computer vision. AI systems can be classified into two main types: narrow AI, which is designed for specific tasks, and general AI, which has the ability to understand and reason about the world like a human."""

result = chain.invoke({"text": text})

print(result)

chain.get_graph().print_ascii()   
