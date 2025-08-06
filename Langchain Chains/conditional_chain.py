from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()  

model = ChatOpenAI()

parser = StrOutputParser()

class feedbackModel(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment classification of the feedback")

parser2 = PydanticOutputParser(pydantic_object=feedbackModel) 

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following text as positive or negetive \n {feedback} \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template="write an appropriate response to this positive feedback \n {feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="write an appropriate response to this negative feedback \n {feedback}",
    input_variables=["feedback"]
)




branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "No response needed for feedback")
)
 
