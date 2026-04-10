from __future__ import annotations
from typing import Optional
from pydantic import BaseModel

class CorpusRecord(BaseModel):
    id: int
    sentence: str
    code: str
    metadata: Optional[dict] = None

class NormalizedRecord(BaseModel):
    id: int
    original_sentence: str
    code: str
    normalized_spaced: str
    normalized_spaceless: str

class IndexEntry:
    __slots__ = ("original_sentence", "code", "record_id")
    def __init__(self, original_sentence: str, code: str, record_id: int) -> None:
        self.original_sentence = original_sentence
        self.code = code
        self.record_id = record_id
    def as_tuple(self) -> tuple[str, str, int]:
        return (self.original_sentence, self.code, self.record_id)