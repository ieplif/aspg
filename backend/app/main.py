from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import login, users, dashboard, receitas, despesas
from app.core.config import settings
from app.core.db import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """ Handle application lifespan events. """
    print("Creating tables...")
    create_db_and_tables()
    print("Tables created!")
    yield
    print("Shutting down...")


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)

    # CORS mais permissivo - IMPORTANTE: Configurar ANTES das rotas
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Em produção, usar settings.BACKEND_CORS_ORIGINS
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["*"],
    )

    _app.include_router(login.router)
    _app.include_router(users.router)
    _app.include_router(dashboard.router)
    _app.include_router(receitas.router)
    _app.include_router(despesas.router)

    return _app


app = get_application()


@app.get("/")
async def root():
    return {"message": "Welcome to ASPG API!"}


# Endpoint para testar CORS
@app.get("/test-cors")
async def test_cors():
    return {"message": "CORS is working!"}