from langchain_community.llms import Ollama

llm = Ollama(model="codestral:latest")

response = llm.invoke("Write a function for fibonacci")

print(response)
