import os

from gotrue.errors import AuthApiError
from supabase import create_client

from app.core.database import get_connection


async def autenticar_en_supabase(email: str, password: str):
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    supabase = create_client(url, key)

    try:
        result = supabase.auth.sign_in_with_password(
            {"email": email, "password": password}
        )
        access_token = result.session.access_token
        user_id = result.user.id
        return {"access_token": access_token, "user_id": user_id}
    except AuthApiError:
        return None


async def obtener_usuario_por_user_id(user_id: str):
    conn = await get_connection()
    query = """
        SELECT
            u.id,
            u.user_id,
            u.rol,
            u.estado,
            u.creado_en,
            p.nombre || ' ' || p.apellido AS nombre,
            o.nombre AS organizacion
        FROM usuario u
        LEFT JOIN persona p ON u.persona_id = p.id
        LEFT JOIN organizacion o ON p.organizacion_id = o.id
        WHERE u.user_id = $1
    """
    result = await conn.fetchrow(query, user_id)
    return result
