from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from schemas.registro import RegistroEntrada, RegistroSalida
from db.deps import get_db
from core.utils import get_client_ip
from services.registro_service import crear_entrada, registrar_salida
from core.deps import get_current_user_id

# Router de registros (entrada/salida)
router = APIRouter(prefix="/registros", tags=["Registros"])

# Endpoint para registrar entrada (inicio de turno)
@router.post("/entrada")
def registrar_entrada(
    data: RegistroEntrada, # Datos enviados (lat, lng, epp)
    request: Request,# Información de la petición (para obtener IP)
    db: Session = Depends(get_db), # Conexión a la DB
    usuario_id: int = Depends(get_current_user_id) # Usuario autenticado desde JWT
):
    try:
        # Obtiene la IP del cliente
        ip = get_client_ip(request)

        # Llama a la lógica de negocio para crear el registro
        registro = crear_entrada(
            db,
            usuario_id,
            data.lat,
            data.lng,
            ip,
            data.epp
        )
        # Retorna confirmación y ID del registro
        return {"message": "Entrada registrada", "registro_id": registro.id}

    except Exception as e:
        # Manejo de errores (ej: ya tiene entrada hoy)
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint para registrar salida (fin de turno)
@router.post("/salida")
def registrar_salida_endpoint(
    data: RegistroSalida,  # Datos enviados (lat, lng)
    request: Request,
    db: Session = Depends(get_db),
    usuario_id: int = Depends(get_current_user_id)
):
    try:
         # Obtiene la IP del cliente
        ip = get_client_ip(request)

        # Llama a la lógica de negocio para cerrar el registro
        registro = registrar_salida(
            db,
            usuario_id,
            data.lat,
            data.lng,
            ip,
            data.motivo,
            data.observacion
        )
        
        # Retorna confirmación
        return {"message": "Salida registrada"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))