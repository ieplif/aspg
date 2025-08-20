FROM python:3.11-slim

WORKDIR /app

# Instalar Poetry
RUN pip install poetry

# Copiar arquivos de configuração
COPY pyproject.toml poetry.lock* ./

# Configurar Poetry e instalar dependências
RUN poetry config virtualenvs.create false \
    && poetry install --only=main --no-root

# Copiar código da aplicação
COPY ./app ./app

# Expor porta
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]