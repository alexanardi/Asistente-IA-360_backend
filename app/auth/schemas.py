from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    email: EmailStr = Field(
        ...,
        description="Correo electrónico registrado del usuario",
        example="demo@asistenteia360.cl",
    )
    password: str = Field(
        ...,
        min_length=6,
        description="Contraseña del usuario (mínimo 6 caracteres)",
        example="demo123456",
    )


class UsuarioOut(BaseModel):
    id: UUID = Field(
        ...,
        example="daae2965-f214-4076-84cb-e086eb3433e9",
        description="ID interno del usuario",
    )
    user_id: UUID = Field(
        ...,
        example="4bc1618a-85e4-433d-b2fe-231c22a54d62",
        description="ID de Supabase Auth",
    )
    rol: str = Field(
        ..., example="user", description="Rol del usuario (admin, user, etc.)"
    )
    estado: str = Field(..., example="activo", description="Estado del usuario")
    nombre: str = Field(
        ..., example="Juan Pérez", description="Nombre completo del usuario"
    )
    organizacion: str = Field(
        ...,
        example="Colegio Nueva Esperanza",
        description="Nombre de la organización del usuario",
    )
    creado_en: datetime = Field(
        ..., example="2025-06-24T01:58:44.167647Z", description="Fecha de creación"
    )


class LoginResponse(BaseModel):
    token: str = Field(
        ...,
        example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
        description="JWT para autenticación",
    )
    usuario: UsuarioOut = Field(..., description="Datos del usuario autenticado")
