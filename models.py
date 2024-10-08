from pydantic import BaseModel


class Document(BaseModel):
    content: str


class URL(Document):
    address: str
