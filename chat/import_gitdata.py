from langchain.vectorstores.weaviate import Weaviate
import weaviate
from langchain_openai import OpenAIEmbeddings

from typing import List


def download_and_chunk(src_url: str, chunk_size: int, overlap_size: int) -> List[str]:
    import requests
    import re

    response = requests.get(src_url)  # Retrieve source text
    source_text = re.sub(r"\s+", " ", response.text)  # Remove multiple whitespaces
    text_words = re.split(r"\s", source_text)  # Split text by single whitespace

    chunks = []
    for i in range(0, len(text_words), chunk_size):  # Iterate through & chunk data
        chunk = " ".join(text_words[max(i - overlap_size, 0): i + chunk_size])  # Join a set of words into a string
        chunks.append(chunk)
    return chunks


pro_git_chapter_url = "https://raw.githubusercontent.com/progit/progit2/main/book/01-introduction/sections/what-is-git.asc"
chunked_text = download_and_chunk(pro_git_chapter_url, 150, 25)


client = weaviate.Client(
    url="http://localhost:8080",
    additional_headers={
        "X-Azure-Api-Key": "402b6da1cb77449db7bd3cd47c252eaf",
#        "Authorization": "Bearer jane-secret-key"
    }
)

collection_name = "GitBookChunk"

client.batch.configure(batch_size=100)
with client.batch as batch:
    for i, chunk in enumerate(chunked_text):
        data_object = {
            "chapter_title": "What is Git",
            "chunk": chunk,
            "chunk_index": i
        }
        batch.add_data_object(data_object=data_object, class_name=collection_name)
