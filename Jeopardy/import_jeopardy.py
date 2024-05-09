import json

import weaviate
import pandas as pd

# Settings for displaying the import progress
counter = 0
interval = 20  # print progress every this many records; should be bigger than the batch_size

client = weaviate.Client(
    url="http://localhost:8080"
)


dataf = open("jeopardy_100.json")

data = json.load(dataf)
dataf.close()
with client.batch(
        batch_size=200,  # Specify batch size
        num_workers=2,   # Parallelize the process
) as batch:
    # Build data objects & add to batch
    for i, row in enumerate(data):
        question_object = {
            "question": row["Question"],
            "answer": row["Answer"],
            "value": row["Value"],
            "round": row["Round"],
            "category": row["Category"],
        }
        batch.add_data_object(
            question_object,
            class_name="JeopardyQuestion"
        )
