# proceder-brain


## 📄 PDF RAG Pipeline

Um pipeline em **Docker Compose** para análise inteligente de PDFs usando o serviço 
[PDF Document Layout Analysis](https://github.com/HURIDOCS/pdf-document-layout-analysis) 
e **LangChain** para perguntas e respostas sobre documentos.

---

## 🚀 O que este projeto faz?
- Processa PDFs com OCR, tabelas, imagens e layout preservado.
- Converte PDFs em **JSON estruturado** com blocos de texto, títulos, tabelas e mais.
- Indexa conteúdo com **LangChain + FAISS**.
- Permite fazer **perguntas sobre o documento** via API.

---

## 🛠️ Stack
- [FastAPI](https://fastapi.tiangolo.com/) – API para upload e Q&A.
- [LangChain](https://www.langchain.com/) – pipeline de embeddings e RAG.
- [FAISS](https://faiss.ai/) – vetor store em memória.
- [SentenceTransformers](https://www.sbert.net/) – embeddings.
- [HURIDOCS PDF Service](https://huggingface.co/spaces/nikita-moor/pdf-document-layout-analysis) – análise de layout e OCR.
- **Docker Compose** – orquestra tudo.

---

## 📦 Como rodar

### 1. Clonar o repositório
```bash
git clone git@github.com:briz-felipe/proceder-brain.git
cd pdf-rag-pipeline
```

### 2. Subir os serviços

```bash
docker compose up --build
```

* PDF Service → [http://localhost:5060](http://localhost:5060)
* API LangChain → [http://localhost:8000](http://localhost:8000/docs)

---

## 🔍 Como usar

### 1. Enviar um PDF

```bash
curl -X POST -F "file=@meu_arquivo.pdf" http://localhost:8000/upload-pdf
```

### 2. Fazer uma pergunta

```bash
curl "http://localhost:8000/ask?query=Qual é o título do documento?"
```

Resposta:

```json
{"query": "Qual é o título do documento?", "answer": "O título é 'Relatório Financeiro 2023'"}
```

---

## 📂 Estrutura do projeto

```
pdf_pipeline/
│
├── docker-compose.yml      # Orquestra os containers
├── pdf-service/            # Serviço de PDF (usa imagem oficial)
└── app/                    # API FastAPI + LangChain
    ├── Dockerfile
    ├── requirements.txt
    └── main.py
```

---

## ⚡ Próximos passos

* Adicionar persistência (FAISS + SQLite ou Pinecone).
* Suporte a múltiplos PDFs.

---

