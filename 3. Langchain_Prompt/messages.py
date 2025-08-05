from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv  
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"  
)
model = ChatHuggingFace(llm=llm)  

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="tell me a joke"),
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)