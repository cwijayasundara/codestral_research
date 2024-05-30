import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

api_key = os.environ["MISTRAL_API_KEY"]

mistral_model = "codestral-latest"

llm = ChatMistralAI(model=mistral_model, temperature=0, api_key=api_key)

response = llm.invoke([("user", "Write a function for fibonacci")])
print(response)
