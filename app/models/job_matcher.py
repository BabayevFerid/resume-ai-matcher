# app/models/job_matcher.py

import logging
from typing import List, Dict, Any
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

logger = logging.getLogger(__name__)


class JobMatcher:
    def __init__(self, resume_text: str, job_postings: List[Dict[str, Any]]):
        self.resume_text = resume_text
        self.job_postings = job_postings
        self.tfidf_vectorizer = TfidfVectorizer(stop_words='english')

    def _prepare_documents(self) -> List[str]:
        """
        Combine resume text and job descriptions into one list for vectorization.
        """
        job_texts = [job["description"] for job in self.job_postings]
        return [self.resume_text] + job_texts

    def match(self, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Match resume against job descriptions and return top-k matches.

        Returns:
            List of matched jobs with similarity scores.
        """
        try:
            documents = self._prepare_documents()
            tfidf_matrix = self.tfidf_vectorizer.fit_transform(documents)
            similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
            top_indices = similarities.argsort()[-top_k:][::-1]

            matches = []
            for idx in top_indices:
                job = self.job_postings[idx]
                matches.append({
                    "title": job["title"],
                    "company": job["company"],
                    "similarity_score": round(float(similarities[idx]), 2),
                    "description": job["description"][:200]  # Short preview
                })

            logger.info(f"Top {top_k} job matches found for resume.")
            return matches
        except Exception as e:
            logger.exception("Error during job matching.")
            raise RuntimeError(f"Job matching failed: {str(e)}")
