# app/services/job_service.py

import json
from pathlib import Path
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)


class JobService:
    def __init__(self, data_path: str = "data/jobs_sample.json"):
        self.data_path = Path(data_path)

    def load_jobs(self) -> List[Dict]:
        """
        Loads job postings from a JSON file and validates the structure.

        Returns:
            List of job dictionaries with title, company, and description.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the job format is invalid.
        """
        if not self.data_path.exists():
            logger.error(f"Job data file not found: {self.data_path}")
            raise FileNotFoundError(f"File not found: {self.data_path}")

        try:
            with open(self.data_path, "r", encoding="utf-8") as file:
                jobs = json.load(file)

            for job in jobs:
                if not all(key in job for key in ("title", "company", "description")):
                    raise ValueError("Invalid job format: Missing required fields")

            logger.info(f"{len(jobs)} job postings loaded successfully.")
            return jobs
        except Exception as e:
            logger.exception("Failed to load job data.")
            raise RuntimeError(f"Error reading job data: {str(e)}")
