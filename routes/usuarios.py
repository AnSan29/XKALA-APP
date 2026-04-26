from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.usuario import UsuarioCreate
from models.usuario import Usuario
from core.security import hash_password
from db.deps import get_db

# Router de usuarios con prefijo /usuarios
router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# Endpoint para crear un nuevo usuario
@router.post("/")
def crear_usuario(data: UsuarioCreate, db: Session = Depends(get_db)):
    # Crea el objeto usuario con los datos recibidos
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
         # La contraseña NO se guarda en texto plano
        password_hash=hash_password(data.password),
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    # Retorna confirmación
    return {"message": "Usuario creado correctamente"}