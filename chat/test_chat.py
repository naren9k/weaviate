from langchain.vectorstores.weaviate import Weaviate
import weaviate
from langchain_openai import OpenAIEmbeddings


client = weaviate.Client(
    url="http://localhost:8080",
#    additional_headers={
#        "Authorization": "Bearer jane-secret-key"
#    }
)

collection_name = "GitBookChunk"

response = client.query.aggregate("GitBookChunk").with_meta_count().do()
print(response)

response = (
    client.query
    .get(class_name=collection_name, properties=["chunk", "chapter_title", "chunk_index"])
    .with_near_text({"concepts": ["history of git"]})
    .with_limit(4)
    .do()
)


response = (
    client.query
    .get(collection_name, ["chunk", "chunk_index"])
    .with_generate(
        single_prompt="Write the following as a haiku: ===== {chunk} "
    )
    .with_limit(3)
    .do()
)

for r in response["data"]["Get"][collection_name]:
    print(f"\n===== Object index: [{r['chunk_index']}] =====")
    print(r["_additional"]["generate"]["singleResult"])
