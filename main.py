from fastapi import FastAPI
from pipelines.indexer import Indexer

app = FastAPI()
indexer = Indexer()


@app.get("/")
def index():
    return "Hello world"


"""
Our core abstraction is called the "Blerb"

A Blerb is created when a user passes a supported file in the form of URLs, PDFs, DOCx, etc.

The Blerb is a page with a Google Office-esque sharing system that provides an easy interface for semantic search,
    question and answering, content summarization and content translation.
"""


@app.get("/blerbify")
def blerbify(target: str):
    """

    Args:
        url (str | None): _description_

    Returns:
        _type_: _description_
    """
    indexer.index(target)
    return target
