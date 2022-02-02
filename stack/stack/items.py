from dataclasses import dataclass


@dataclass
class StackItem:
    _id: str
    author: str
    title: str
    url: str
    published: str
