"""The ingest pipeline preprocesses files based on the type."""

from haystack import Pipeline
from haystack.components.converters import HTMLToDocument
from haystack.components.fetchers import LinkContentFetcher
from haystack.components.writers import DocumentWriter
from haystack.document_stores.in_memory import InMemoryDocumentStore


class Indexer:
    def __init__(self):
        document_store = InMemoryDocumentStore()
        fetcher = LinkContentFetcher()
        converter = HTMLToDocument()
        writer = DocumentWriter(document_store=document_store)

        self.indexing_pipeline = Pipeline()
        self.indexing_pipeline.add_component(instance=fetcher, name="fetcher")
        self.indexing_pipeline.add_component(instance=converter, name="converter")
        self.indexing_pipeline.add_component(instance=writer, name="writer")

        self.indexing_pipeline.connect("fetcher.streams", "converter.sources")
        self.indexing_pipeline.connect("converter.documents", "writer.documents")

    def index(self, url: str) -> None:
        self.indexing_pipeline.run(data={"fetcher": {"urls": [url]}})
