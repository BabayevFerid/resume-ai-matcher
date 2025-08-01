# app/main.py

from fastapi import FastAPI
from app.api.endpoints import router as resume_router
import logging
import uvicorn

# Logging konfiqurasiyası
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

# FastAPI tətbiqi
app = FastAPI(
    title="AI-Powered Resume Matcher",
    description="Verilən CV mətninə əsasən uyğun vakansiyalar tapır",
    version="1.0.0"
)

# Router əlavə olunur
app.include_router(resume_router, prefix="/api", tags=["Resume Matcher"])

# Serveri birbaşa burdan işə salmaq istəsən
if __name__ == "__main__":
    logger.info("Starting Resume Matcher API...")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
