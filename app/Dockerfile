FROM python:3.10-slim

# Definir variáveis de ambiente para otimizar o comportamento do Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Criar e usar um diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema necessárias para o Python e limpar o cache
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependências do Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação
COPY . .

# Criar um usuário não-root e trocar para ele
RUN useradd -m appuser
USER appuser

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
