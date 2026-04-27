from pydantic import BaseModel
from typing import Optional

# Esquema para los Elementos de Protección Personal (EPP)
class EPP(BaseModel):
    casco: bool
    gafas: bool
    reflectivo: bool
    botas: bool
    arnes: bool

# Datos necesarios para registrar entrada (inicio de turno)
class RegistroEntrada(BaseModel):
    lat: float
    lng: float
    epp: EPP

# Datos necesarios para registrar salida (fin de turno)
class RegistroSalida(BaseModel):
    lat: float
    lng: float
    motivo: str
    observacion: Optional[str] = None

    