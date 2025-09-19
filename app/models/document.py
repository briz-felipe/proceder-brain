from langchain.schema import Document
from typing import List, Dict, Any

class DocumentProcessor:
    @staticmethod
    def create_documents(elements: List[Dict[str, Any]]) -> List[Document]:
        docs = []
        for element in elements:
            text = element.get("text", "")
            if text.strip():
                metadata = {
                    "page": element.get("page_num"),
                    "type": element.get("type"),
                }
                docs.append(Document(page_content=text, metadata=metadata))
        return docs