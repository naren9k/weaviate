from langchain.vectorstores.weaviate import Weaviate
import weaviate
from langchain_openai import OpenAIEmbeddings


client = weaviate.Client(
    url="http://localhost:8080",
    additional_headers={
        "X-Azure-Api-Key": "402b6da1cb77449db7bd3cd47c252eaf"
    }
)

collection_name = "GitBookChunk"

chunk_class = {
    "class": collection_name,
    "properties": [
        {
            "name": "chunk",
            "dataType": ["text"],
        },
        {
            "name": "chapter_title",
            "dataType": ["text"],
        },
        {
            "name": "chunk_index",
            "dataType": ["int"],
        }
    ],
    "vectorizer": "text2vec-openai",
    "moduleConfig": {
        "text2vec-openai": {
            "resourceName": "oai-bispoc-dev-001",
            "deploymentId": "embedding-ada-002",
            "vectorizeClassName": False,
            "base_url": "https://oai-bispoc-dev-001.openai.azure.com/",
            "model": "ada",
            "modelVersion": "002",
            "type": "text"
        },
        "generative-openai": {
            "resourceName": "oai-bispoc-dev-001",
            "deploymentId": "gpt35turbo16k",
            "base_url": "https://oai-bispoc-dev-001.openai.azure.com/",
            "model": "gpt-3.5-turbo-16k",
        }
    }
}

if client.schema.exists(collection_name):  # In case we've created this collection before
    client.schema.delete_class(collection_name)  # THIS WILL DELETE ALL DATA IN THE CLASS

client.schema.create_class(chunk_class)
