# app/models/resume_parser.py

import pdfplumber
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class ResumeParser:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def extract_text(self) -> str:
        """
        Extracts text from a given PDF resume.

        Returns:
            Extracted text as a string.
        Raises:
            FileNotFoundError: If the file path is invalid.
            Exception: For other unknown errors.
        """
        if not self.file_path.exists():
            logger.error(f"File not found: {self.file_path}")
            raise FileNotFoundError(f"Resume file not found: {self.file_path}")

        try:
            text = ""
            with pdfplumber.open(str(self.file_path)) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            logger.info(f"Successfully extracted text from: {self.file_path.name}")
            return text.strip()
        except Exception as e:
            logger.exception("Failed to extract text from resume")
            raise RuntimeError(f"Error extracting resume text: {str(e)}")
