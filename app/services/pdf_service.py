import requests
from typing import Dict, Any
from ..core.config import settings

class PDFService:
    def __init__(self):
        self.base_url = settings.pdf_service_url
    
    async def process_pdf(self, filename: str, file_content: bytes, content_type: str) -> Dict[str, Any]:
        files = {"file": (filename, file_content, content_type)}
        response = requests.post(self.base_url, files=files)
        response.raise_for_status()
        return response.json()