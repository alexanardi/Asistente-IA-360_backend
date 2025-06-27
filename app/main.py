import os

from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import RedirectResponse

from app.auth import router as auth_router

ENVIRONMENT = os.getenv("ENVIRONMENT", "production")

from app.auth.dependencies import get_current_user

app = FastAPI(
    title="Asistente IA 360",
    docs_url=None,
    redoc_url=None,
    openapi_url="/openapi.json",
)


# Documentación solo en desarrollo o protegida
if ENVIRONMENT == "development":

    @app.get("/docs", include_in_schema=False)
    async def swagger_ui():
        return get_swagger_ui_html(
            openapi_url="/openapi.json", title="Documentación (Dev)"
        )

else:

    @app.get("/docs", include_in_schema=False)
    async def swagger_ui(user=Depends(get_current_user)):
        return get_swagger_ui_html(
            openapi_url="/openapi.json", title="Documentación protegida"
        )


origins = [
    "http://localhost:3000",  # en desarrollo
    "https://asistente-ia-360-backend.up.railway.app",  # en producción
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

app.include_router(auth_router.router)
