from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class PDFElement(BaseModel):
    text: str
    page_num: int
    type: str
    metadata: Optional[Dict[str, Any]] = None

class PDFProcessResponse(BaseModel):
    elements: List[PDFElement]

class UploadResponse(BaseModel):
    message: str
    chunks: int
    filename: str

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    query: str
    answer: str
    sources: Optional[List[str]] = None