from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.usuario import UsuarioCreate
from models.usuario import Usuario
from core.security import hash_password
from db.deps import get_db
from core.deps import get_current_user

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


# ✅ CREAR USUARIO
@router.post("/")
def crear_usuario(data: UsuarioCreate, db: Session = Depends(get_db)):
    nuevo_usuario = Usuario(
        nombres=data.nombres,
        apellidos=data.apellidos,
        tipo_documento_id=data.tipo_documento_id,
        documento=data.documento,
        grupo_sanguineo=data.grupo_sanguineo,
        eps_id=data.eps_id,
        arl_id=data.arl_id,
        cargo_id=data.cargo_id,
        telefono=data.telefono,
        email=data.email,
        password_hash=hash_password(data.password),
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return {"message": "Usuario creado correctamente"}


# USUARIO ACTUAL
@router.get("/me")
def obtener_usuario_actual(current_user: Usuario = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "nombres": current_user.nombres,
        "apellidos": current_user.apellidos,
        "email": current_user.email,
    }