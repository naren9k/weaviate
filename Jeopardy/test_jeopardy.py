import weaviate
import json

client = weaviate.Client(
    url="http://localhost:8080"
)

where_filter = {
    "path": ["category"],
    "operator": "Equal",
    "valueText": "ANIMALS",
}



result = (
    client.query
    .get("JeopardyQuestion", ["question", "answer", "category"])
    .with_near_text({"concepts": ["biology"]})
    .with_where(where_filter)
    .do()
)

print(json.dumps(result, indent=4))

assert client.query.aggregate("JeopardyQuestion").with_meta_count().do()

#print("Connecting")
#client.connect()
#print("Connected")

#questions = client.collections.get("Jeopardy")
#questions.query()

#assert client.query.aggregate("JeopardyQuestion").with_meta_count().do()["data"]["Aggregate"]["JeopardyQuestion"][0]["meta"]["count"] == 100
