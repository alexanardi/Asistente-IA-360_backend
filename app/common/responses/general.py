from fastapi import status

general_responses = {
    status.HTTP_500_INTERNAL_SERVER_ERROR: {
        "description": "Error interno del servidor.",
        "content": {
            "application/json": {"example": {"detail": "Ocurrió un error inesperado"}}
        },
    }
}
