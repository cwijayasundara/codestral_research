import os
from dotenv import load_dotenv

from mistralai.client import MistralClient

load_dotenv()

api_key = os.environ["MISTRAL_API_KEY"]

client = MistralClient(api_key=api_key)

model = "codestral-latest"

prompt = "def fibonacci(n: int):"
suffix = "n = int(input('Enter a number: '))\nprint(fibonacci(n))"

response = client.completion(
    model=model,
    prompt=prompt,
    suffix=suffix,
)

print(
    f"""
{prompt}
{response.choices[0].message.content}
{suffix}
"""
)
