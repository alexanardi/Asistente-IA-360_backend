from fastapi import APIRouter

from app.auth.schemas import LoginRequest, LoginResponse
from app.auth.service import login_usuario
from app.common.responses.auth import auth_responses
from app.common.responses.general import general_responses
from app.common.responses.validation import validation_response

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
    "/login",
    response_model=LoginResponse,
    responses={**auth_responses, **validation_response, **general_responses},
    summary="Autenticación de usuario",
    description="Permite iniciar sesión con correo y contraseña registrados.",
)
async def login(request: LoginRequest):
    return await login_usuario(request.email, request.password)
