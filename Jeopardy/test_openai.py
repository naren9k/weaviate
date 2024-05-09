import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="402b6da1cb77449db7bd3cd47c252eaf",
    api_version="2023-05-15",
    azure_endpoint="https://oai-bispoc-dev-001.openai.azure.com/"
)

response = client.embeddings.create(
    input="Your text string goes here",
    model="embedding-ada-002"
)

print(response.model_dump_json(indent=2))
