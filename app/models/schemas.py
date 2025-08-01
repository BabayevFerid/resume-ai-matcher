# app/models/schemas.py

from pydantic import BaseModel, Field
from typing import List


class JobPosting(BaseModel):
    title: str
    company: str
    description: str


class MatchResult(BaseModel):
    title: str
    company: str
    similarity_score: float = Field(..., ge=0, le=1)
    description: str


class ResumeMatchRequest(BaseModel):
    resume_text: str
    job_postings: List[JobPosting]
    top_k: int = Field(default=3, ge=1, le=10)


class ResumeMatchResponse(BaseModel):
    matches: List[MatchResult]
