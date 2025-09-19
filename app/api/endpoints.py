from fastapi import APIRouter, UploadFile, HTTPException
from ..schemas.pdf import UploadResponse, QueryResponse
from ..services.pdf_service import PDFService
from ..services.vector_service import VectorService
from ..models.document import DocumentProcessor

router = APIRouter()
pdf_service = PDFService()
vector_service = VectorService()

@router.post("/upload-pdf", response_model=UploadResponse)
async def upload_pdf(file: UploadFile):
    try:
        file_content = await file.read()
        pdf_data = await pdf_service.process_pdf(file.filename, file_content, file.content_type)
        
        documents = DocumentProcessor.create_documents(pdf_data.get("elements", []))
        chunks_count = vector_service.process_documents(documents)
        
        return UploadResponse(
            message=f"PDF {file.filename} processado com sucesso",
            chunks=chunks_count,
            filename=file.filename
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/ask", response_model=QueryResponse)
async def ask(query: str):
    try:
        answer = vector_service.query(query)
        return QueryResponse(query=query, answer=answer)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))