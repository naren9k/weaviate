import weaviate

client = weaviate.Client(
    url="http://localhost:8080"
)

client.schema.delete_class("JeopardyQuestion")

class_obj = {
    # Class & property definitions
    "class": "JeopardyQuestion",
    "properties": [
        {
            "name": "round",
            "dataType": ["text"],
            # Property-level module configuration for `round`
            "moduleConfig": {
                "text2vec-openai": {
                    "skip": True,
                }
            },
            # End of property-level module configuration
        },
        {
            "name": "value",
            "dataType": ["int"],
        },
        {
            "name": "question",
            "dataType": ["text"],
        },
        {
            "name": "category",
            "dataType": ["text"],
        },
        {
            "name": "answer",
            "dataType": ["text"],
        },
    ],

    # Specify a vectorizer
    "vectorizer": "text2vec-openai",

    # Module settings
    "moduleConfig": {
        "text2vec-openai": {
            "resourceName": "oai-bispoc-dev-001",
            #"deploymentId": "embedding-ada-002",
            "deploymentId": "embedding-ada-002",
            "vectorizeClassName": False,
            "base_url": "https://oai-bispoc-dev-001.openai.azure.com/",
            "model": "ada",
            "modelVersion": "002",
            "type": "text"
        }
    },
}
# End class definition

client.schema.create_class(class_obj)
