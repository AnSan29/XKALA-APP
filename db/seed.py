from db import init_models
from sqlalchemy.orm import Session
from db.session import SessionLocal

from models.catalogos import TipoDocumento, EPS, ARL, Cargo


#  Inserta tipos de documento si no existen
def seed_tipos_documento(db: Session):
    data = ["CC", "TI", "CE"]

    for nombre in data:
        # Verifica si ya existe para evitar duplicados
        exists = db.query(TipoDocumento).filter_by(nombre=nombre).first()
        if not exists:
            db.add(TipoDocumento(nombre=nombre))

# Inserta EPS si no existen
def seed_eps(db: Session):
    data = ["Sura", "Sanitas", "Nueva EPS"]

    for nombre in data:
        exists = db.query(EPS).filter_by(nombre=nombre).first()
        if not exists:
            db.add(EPS(nombre=nombre))

# Inserta ARL si no existen
def seed_arl(db: Session):
    data = ["Sura", "Bolivar"]

    for nombre in data:
        exists = db.query(ARL).filter_by(nombre=nombre).first()
        if not exists:
            db.add(ARL(nombre=nombre))

# Inserta cargos si no existen
def seed_cargos(db: Session):
    data = ["Obrero", "Supervisor", "Ingeniero"]

    for nombre in data:
        exists = db.query(Cargo).filter_by(nombre=nombre).first()
        if not exists:
            db.add(Cargo(nombre=nombre))

# Ejecuta todos los seeders
def run_seed():
    db = SessionLocal()

    try:
        seed_tipos_documento(db)
        seed_eps(db)
        seed_arl(db)
        seed_cargos(db)

        db.commit()
        print("Seed ejecutado correctamente")

    except Exception as e:
        db.rollback()
        print("❌ Error en seed:", e)

    finally:
        db.close()

# Permite ejecutar el archivo directamente desde terminal
if __name__ == "__main__":
    run_seed()