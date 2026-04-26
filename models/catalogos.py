from sqlalchemy import Column, Integer, String
from db.base import Base

class TipoDocumento(Base):
    __tablename__ = "tipos_documento"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False, unique=True)

class EPS(Base):
    __tablename__ = "eps"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, unique=True)


class ARL(Base):
    __tablename__ = "arl"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, unique=True)


class Cargo(Base):
    __tablename__ = "cargos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, unique=True)