from fastapi import status

validation_response = {
    status.HTTP_422_UNPROCESSABLE_ENTITY: {
        "description": "Error de validación de los datos enviados.",
        "content": {
            "application/json": {
                "example": {
                    "detail": [
                        {
                            "loc": ["body", "email"],
                            "msg": "El valor no es una dirección de correo electrónico válida",
                            "type": "value_error.email",
                        },
                        {
                            "loc": ["body", "password"],
                            "msg": "Asegúrese de que este valor tenga al menos 6 caracteres",
                            "type": "value_error.any_str.min_length",
                        },
                    ]
                }
            }
        },
    }
}
