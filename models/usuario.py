from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)

    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)

    tipo_documento_id = Column(Integer, ForeignKey("tipos_documento.id"))
    documento = Column(String(50), unique=True, nullable=False)

    grupo_sanguineo = Column(String(5))

    eps_id = Column(Integer, ForeignKey("eps.id"))
    arl_id = Column(Integer, ForeignKey("arl.id"))
    cargo_id = Column(Integer, ForeignKey("cargos.id"))

    telefono = Column(String(20))
    email = Column(String(100))

    password_hash = Column(String(255), nullable=False)

    activo = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relaciones (no obligatorias, pero útiles)
    tipo_documento = relationship("TipoDocumento")
    eps = relationship("EPS")
    arl = relationship("ARL")
    cargo = relationship("Cargo")