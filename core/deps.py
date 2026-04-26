from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from core.security import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Dependencia que se usa en rutas protegidas
def get_current_user_id(token: str = Depends(oauth2_scheme)):
    # Decodifica el token y obtiene el user_id
    user_id = decode_token(token)

    # Si el token es inválido o expiró, no permite acceso
    if not user_id:
        raise HTTPException(status_code=401, detail="Token inválido")

    # Retorna el ID del usuario autenticado
    return int(user_id)