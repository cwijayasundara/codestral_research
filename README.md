This repo contains some research using Mistrals Codestral (https://mistral.ai/news/codestral/) which is a 22B parameter 
model.

You need the following to run the code:

- Python 3.11
- Codestral API key : https://console.mistral.ai/codestral
- Or you can install Codestral locally: in Ollama (ollama run codestral)
  - Ollama model does not run in M1 Macs with 16 GB RAM with Ollama version 0.1.39. Looks like they had fixed this in 0.1.40
- create a .env file with the following content:
```
MISTRAL_API_KEY=''
LANGCHAIN_API_KEY=''
```

- install all the requirements in requirements.txt
```
pip install -r requirements.txt
``` 
- App in the /code_generator folder is a streamlit app that generates complete microservices code using Codestral.
- you can run the code in the following way:
```
cd code_generator
streamlit run app.py
``` 
- There is a self-correcting code generator inspired by Langchains https://www.youtube.com/watch?v=zXFxmI9f06M&t=24s
- Planning to add more features to the self-correcting code generator
```
cd self_corrective_codegen
python self_corrective_code_gen.py
``` 
