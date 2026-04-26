from sqlalchemy.orm import Session
from datetime import date 
from models.registro import Registro
from models.epp import RegistroEPP
from datetime import datetime

# Crea el registro de entrada (inicio de turno)
def crear_entrada(db: Session, usuario_id: int, lat: float, lng: float, ip: str, epp_data):
    
    #  Fecha actual
    hoy = date.today()
    # 🔍 Verifica si ya existe un registro abierto hoy
    registro_existente = db.query(Registro).filter(
        Registro.usuario_id == usuario_id,
        Registro.fecha == hoy,
        Registro.cerrado == False
    ).first()
    #  No permite doble entrada el mismo día
    if registro_existente:
        raise Exception("Ya existe un registro de entrada abierto hoy")

    # Crea el registro de entrada
    nuevo_registro = Registro(
        usuario_id=usuario_id,
        lat_entrada=lat,
        lng_entrada=lng,
        ip_entrada=ip
    )

    db.add(nuevo_registro)
    db.commit()
    db.refresh(nuevo_registro)

    # Guarda el checklist de EPP asociado al registro
    epp = RegistroEPP(
        registro_id=nuevo_registro.id,
        casco=epp_data.casco,
        gafas=epp_data.gafas,
        reflectivo=epp_data.reflectivo,
        botas=epp_data.botas,
        arnes=epp_data.arnes
    )

    db.add(epp)
    db.commit()
    # Retorna el registro creado
    return nuevo_registro


# Registra la salida (fin de turno)
def registrar_salida(db, usuario_id: int, lat: float, lng: float, ip: str):
    # Fecha actual
    hoy = date.today()
    # Busca el registro abierto del día
    registro = db.query(Registro).filter(
        Registro.usuario_id == usuario_id,
        Registro.fecha == hoy,
        Registro.cerrado == False
    ).first()
    # Si no hay entrada previa, no permite salida
    if not registro:
        raise Exception("No hay registro de entrada activo hoy")
     # Actualiza datos de salida
    registro.hora_salida = datetime.utcnow()
    registro.lat_salida = lat
    registro.lng_salida = lng
    registro.ip_salida = ip
    # Marca el turno como cerrado
    registro.cerrado = True

    # Guarda cambios
    db.commit()

    # Retorna el registro actualizado
    return registro