from fastapi import HTTPException

from app.auth.repository import autenticar_en_supabase, obtener_usuario_por_user_id
from app.auth.schemas import LoginResponse, UsuarioOut


async def login_usuario(email: str, password: str) -> LoginResponse:
    resultado = await autenticar_en_supabase(email, password)

    if not resultado or "user_id" not in resultado or "access_token" not in resultado:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    user_id = resultado["user_id"]
    token = resultado["access_token"]

    usuario = await obtener_usuario_por_user_id(user_id)

    if not usuario:
        raise HTTPException(
            status_code=404, detail="Usuario no registrado en la plataforma"
        )

    if usuario["estado"] != "activo":
        raise HTTPException(status_code=403, detail="Usuario inactivo")

    return LoginResponse(token=token, usuario=UsuarioOut(**usuario))
