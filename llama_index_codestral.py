import os
from dotenv import load_dotenv
from llama_index.core.llms import ChatMessage
from llama_index.llms.mistralai import MistralAI

load_dotenv()

api_key = os.environ["MISTRAL_API_KEY"]

mistral_model = "codestral-latest"

messages = [
    ChatMessage(role="user", content="Write a function for fibonacci"),
]
response = MistralAI(api_key=api_key, model=mistral_model).chat(messages)
print(response)
