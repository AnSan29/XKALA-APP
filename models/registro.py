from sqlalchemy import Column, Integer, ForeignKey, Date, DateTime, Float, String, Boolean
from datetime import datetime, date
from db.base import Base


class Registro(Base):
    __tablename__ = "registros"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    fecha = Column(Date, default=date.today)

    # Entrada
    hora_entrada = Column(DateTime, default=datetime.utcnow)
    lat_entrada = Column(Float)
    lng_entrada = Column(Float)
    ip_entrada = Column(String(50))

    # Salida
    hora_salida = Column(DateTime, nullable=True)
    lat_salida = Column(Float, nullable=True)
    lng_salida = Column(Float, nullable=True)
    ip_salida = Column(String(50), nullable=True)

    cerrado = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)