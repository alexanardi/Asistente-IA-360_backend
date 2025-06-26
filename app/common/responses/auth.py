from fastapi import status

auth_responses = {
    status.HTTP_401_UNAUTHORIZED: {
        "description": "Credenciales inválidas",
        "content": {
            "application/json": {"example": {"detail": "Credenciales inválidas"}}
        },
    },
    status.HTTP_403_FORBIDDEN: {
        "description": "Usuario inactivo",
        "content": {"application/json": {"example": {"detail": "Usuario inactivo"}}},
    },
    status.HTTP_404_NOT_FOUND: {
        "description": "Usuario no registrado en la plataforma",
        "content": {
            "application/json": {
                "example": {"detail": "Usuario no registrado en la plataforma"}
            }
        },
    },
}
