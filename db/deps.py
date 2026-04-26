from db.session import SessionLocal

# Dependencia para obtener una sesión de base de datos en cada request
def get_db():
     # Crea una nueva conexión (sesión)
    db = SessionLocal()
    try:
        # Entrega la sesión a la ruta que la necesite
        yield db
    finally:
        # Cierra la conexión cuando termina la petición
        db.close()