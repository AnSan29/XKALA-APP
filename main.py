# Framework principal
from fastapi import FastAPI
# Conexión a la base de datos
from db.session import engine
# Clase base de los modelos
from db.base import Base
from db import init_models  
# Rutas de la aplicación
from routes import auth, usuarios
from routes import registros

# Instancia principal de FastAPI
app = FastAPI()

#Evento que se ejecuta al iniciar la aplicación
@app.on_event("startup")
def startup():
    print("Creando tablas...")
    # Crea las tablas en la base de datos si no existen
    Base.metadata.create_all(bind=engine)

# Endpoint raíz (prueba básica)
@app.get("/")
def root():
    return {"message": "API funcionando"}


# Registro de rutas en la aplicación
app.include_router(auth.router) # Autenticación (/auth)
app.include_router(usuarios.router)  # Usuarios (/usuarios)
app.include_router(registros.router) # Registros (/registros)

    