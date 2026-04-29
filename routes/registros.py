from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from datetime import date

from schemas.registro import RegistroEntrada, RegistroSalida
from models.registro import Registro
from models.usuario import Usuario

from db.deps import get_db
from core.utils import get_client_ip
from services.registro_service import crear_entrada, registrar_salida
from core.deps import get_current_user

# Router de registros (entrada/salida)
router = APIRouter(prefix="/registros", tags=["Registros"])


# ✅ REGISTRAR ENTRADA
@router.post("/entrada")
def registrar_entrada(
    data: RegistroEntrada,
    request: Request,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user),  # 👈 CAMBIO CLAVE
):
    try:
        ip = get_client_ip(request)

        registro = crear_entrada(
            db,
            current_user.id,  # 👈 usamos el id desde el usuario
            data.lat,
            data.lng,
            ip,
            data.epp
        )

        return {"message": "Entrada registrada", "registro_id": registro.id}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ✅ REGISTRAR SALIDA
@router.post("/salida")
def registrar_salida_endpoint(
    data: RegistroSalida,
    request: Request,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user),  # 👈 CAMBIO
):
    try:
        ip = get_client_ip(request)

        registro = registrar_salida(
            db,
            current_user.id,  # 👈 igual aquí
            data.lat,
            data.lng,
            ip,
            data.motivo,
            data.observacion
        )

        return {"message": "Salida registrada"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ✅ CONSULTAR ESTADO ACTUAL
@router.get("/estado")
def consultar_estado(
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user),  # 👈 CAMBIO
):
    hoy = date.today()

    registro = db.query(Registro).filter(
        Registro.usuario_id == current_user.id,  # 👈 CAMBIO
        Registro.fecha == hoy,
        Registro.cerrado == False
    ).first()

    return {"activo": True if registro else False}