from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.auth import LoginRequest
from services.auth_service import authenticate_user
from db.deps import get_db

# Define el router de autenticación con prefijo /auth
router = APIRouter(prefix="/auth", tags=["Auth"])

# Endpoint de login
@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
     # Intenta autenticar al usuario con documento y contraseña
    token = authenticate_user(db, data.documento, data.password)
     # Si las credenciales son incorrectas, bloquea el acceso
    if not token:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    # Retorna el token JWT para futuras peticiones autenticadas
    return {"access_token": token, "token_type": "bearer"}