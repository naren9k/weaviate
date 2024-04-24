import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="402b6da1cb77449db7bd3cd47c252eaf",
    api_version="2023-05-15",
    azure_endpoint="https://oai-bispoc-dev-001.openai.azure.com/"
)

#response = client.embeddings.create(
#    input="Your text string goes here",
#    model="embedding-ada-002"
#)

#print(response.model_dump_json(indent=2))



# response = client.chat.completions.create(
#     model="embedding-ada-002",
#     #model="gpt-35-turbo-16k",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Who won the world series in 2020?"},
#         {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#         {"role": "user", "content": "Where was it played?"}
#     ]
# )

response = client.chat.completions.create(
    model="gpt-35-turbo-16k", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
        {"role": "user", "content": "Who were the founders of Microsoft?"}
    ]
)

#print(response)
print(response.model_dump_json(indent=2))
print(response.choices[0].message.content)
