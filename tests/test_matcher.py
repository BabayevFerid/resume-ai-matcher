# tests/test_matcher.py

import pytest
from app.models.job_matcher import JobMatcher

@pytest.fixture
def sample_resume_text():
    return """
    Experienced machine learning engineer with strong Python, TensorFlow, and data analysis skills.
    Worked on NLP projects and deployed models to production environments.
    """

@pytest.fixture
def sample_job_postings():
    return [
        {
            "title": "Machine Learning Engineer",
            "company": "TechCorp",
            "description": "Looking for an ML engineer with experience in Python, TensorFlow, and model deployment."
        },
        {
            "title": "Data Analyst",
            "company": "DataX",
            "description": "Seeking data analyst with experience in Excel and BI tools."
        },
        {
            "title": "NLP Researcher",
            "company": "AI Labs",
            "description": "Requires NLP skills, deep learning experience, and proficiency in PyTorch."
        }
    ]

def test_matcher_returns_top_k_results(sample_resume_text, sample_job_postings):
    matcher = JobMatcher(resume_text=sample_resume_text, job_postings=sample_job_postings)
    results = matcher.match(top_k=2)

    assert len(results) == 2
    assert results[0]["similarity_score"] >= results[1]["similarity_score"]

def test_matcher_result_fields(sample_resume_text, sample_job_postings):
    matcher = JobMatcher(resume_text=sample_resume_text, job_postings=sample_job_postings)
    result = matcher.match(top_k=1)[0]

    assert "title" in result
    assert "company" in result
    assert "similarity_score" in result
    assert isinstance(result["similarity_score"], float)
