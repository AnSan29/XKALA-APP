from sqlalchemy.orm import Session
from models.usuario import Usuario
from core.security import verify_password, create_access_token

# Autentica al usuario y genera un token si es válido
def authenticate_user(db: Session, documento: str, password: str):
    # Busca el usuario por documento
    user = db.query(Usuario).filter(Usuario.documento == documento).first()
    # Si no existe, no permite acceso
    if not user:
        return None
    # Verifica que la contraseña coincida con el hash almacenado
    if not verify_password(password, user.password_hash):
        return None
    # Crea un token JWT con el ID del usuario
    token = create_access_token({"sub": str(user.id)})
    # Retorna el token para autenticación futura
    return token