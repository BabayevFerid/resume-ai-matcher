# app/api/endpoints.py

from fastapi import APIRouter, HTTPException
from app.models.schemas import ResumeMatchRequest, ResumeMatchResponse
from app.models.job_matcher import JobMatcher
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/match/", response_model=ResumeMatchResponse)
def match_resume_to_jobs(request: ResumeMatchRequest):
    """
    API endpoint to match a resume against job postings using NLP similarity.
    """
    try:
        matcher = JobMatcher(resume_text=request.resume_text, job_postings=request.job_postings)
        results = matcher.match(top_k=request.top_k)
        return ResumeMatchResponse(matches=results)
    except Exception as e:
        logger.exception("Matching failed in /match/ endpoint.")
        raise HTTPException(status_code=500, detail="Internal Server Error")
