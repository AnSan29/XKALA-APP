from pydantic import BaseModel

# Esquema de datos para el login
class LoginRequest(BaseModel):
    # Documento del usuario (ej: cédula)
    documento: str
    #  Contraseña del usuario
    password: str