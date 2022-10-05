from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app import api_router
from core.config import settings
from db import init_db, SessionLocal

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)


def init() -> None:
    db = SessionLocal()
    init_db(db)

def main() -> None:
    db = SessionLocal()
    init()

if __name__ == "__main__":
    main()
