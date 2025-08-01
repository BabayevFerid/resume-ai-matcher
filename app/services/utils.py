# app/services/utils.py

import os
from pathlib import Path
import uuid
import logging

logger = logging.getLogger(__name__)


def save_temp_file(file_bytes: bytes, extension: str = ".pdf") -> Path:
    """
    Saves uploaded file content to a temporary file and returns the path.

    Args:
        file_bytes (bytes): File content.
        extension (str): File extension (default is .pdf).

    Returns:
        Path: The path to the saved temporary file.
    """
    try:
        filename = f"temp_{uuid.uuid4().hex}{extension}"
        temp_dir = Path("temp_files")
        temp_dir.mkdir(exist_ok=True)
        temp_path = temp_dir / filename

        with open(temp_path, "wb") as f:
            f.write(file_bytes)

        logger.info(f"Temporary file saved: {temp_path}")
        return temp_path
    except Exception as e:
        logger.exception("Error saving temporary file")
        raise RuntimeError(f"Failed to save file: {str(e)}")


def clean_temp_files():
    """
    Cleans up temporary files created during processing.
    """
    try:
        temp_dir = Path("temp_files")
        if temp_dir.exists():
            for f in temp_dir.iterdir():
                if f.is_file():
                    f.unlink()
            logger.info("Temporary files cleaned.")
    except Exception as e:
        logger.warning(f"Failed to clean temp files: {str(e)}")
