from typing import Optional, List
from pydantic import BaseModel, Field

class SearchRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=500)
    fuzzy_threshold: Optional[int] = Field(None, ge=0, le=100)

class SearchResponse(BaseModel):
    input: str
    matched_sentence: Optional[str] = None
    code: Optional[str] = None
    match_score: Optional[float] = None
    match_type: str
    latency_ms: float

class BatchSearchRequest(BaseModel):
    queries: List[str] = Field(..., min_length=1, max_length=1000)
    fuzzy_threshold: Optional[int] = Field(None, ge=0, le=100)

class BatchSearchResponse(BaseModel):
    results: List[SearchResponse]
    total: int
    latency_ms: float

class HealthResponse(BaseModel):
    status: str
    index_size: int
    uptime_seconds: float
    version: str = "0.1.0"