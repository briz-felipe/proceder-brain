from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from typing import List, Optional
from core.config import settings

class VectorService:
    def __init__(self):
        self.embedding_model = SentenceTransformerEmbeddings(model_name=settings.embedding_model)
        self.vectorstore: Optional[FAISS] = None
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap
        )
    
    def process_documents(self, documents: List[Document]) -> int:
        chunks = self.text_splitter.split_documents(documents)
        self.vectorstore = FAISS.from_documents(chunks, self.embedding_model)
        return len(chunks)
    
    def query(self, question: str) -> str:
        if not self.vectorstore:
            raise ValueError("No documents processed yet")
        
        retriever = self.vectorstore.as_retriever()
        llm = OpenAI(temperature=0)
        qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
        return qa.run(question)