common_responses = {
    401: {
        "description": "Credenciales inválidas",
        "content": {
            "application/json": {"example": {"detail": "Credenciales inválidas"}}
        },
    },
    403: {
        "description": "Acceso prohibido / Usuario inactivo",
        "content": {"application/json": {"example": {"detail": "Usuario inactivo"}}},
    },
    404: {
        "description": "Recurso no encontrado",
        "content": {
            "application/json": {
                "example": {"detail": "Usuario no registrado en la plataforma"}
            }
        },
    },
}
