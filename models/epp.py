from sqlalchemy import Column, Integer, ForeignKey, Boolean, DateTime
from datetime import datetime
from db.base import Base


class RegistroEPP(Base):
    __tablename__ = "registro_epp"

    id = Column(Integer, primary_key=True, index=True)

    registro_id = Column(Integer, ForeignKey("registros.id"))

    casco = Column(Boolean, default=False)
    gafas = Column(Boolean, default=False)
    reflectivo = Column(Boolean, default=False)
    botas = Column(Boolean, default=False)
    arnes = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)