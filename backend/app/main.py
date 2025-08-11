from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import login, users
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

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(login.router)
    _app.include_router(users.router)

    return _app


app = get_application()


@app.get("/")
async def root():
    return {"message": "Welcome to ASPG API!"}
