from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

 # Crea el motor de conexión a la base de datos
engine = create_engine(settings.DATABASE_URL)

# Creador de sesiones de base de datos
SessionLocal = sessionmaker(
    autocommit=False,   # No guarda automáticamente (se usa db.commit() manual)
    autoflush=False,    # No envía cambios automáticamente (control manual)
    bind=engine         # Conecta las sesiones al motor de la DB
)