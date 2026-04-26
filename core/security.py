from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from core.config import settings

# Configuración del algoritmo de hash (bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hashea la contraseña antes de guardarla en la DB
def hash_password(password: str):
    return pwd_context.hash(password)

# Verifica si una contraseña ingresada coincide con la almacenada
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Crea un token JWT con datos del usuario (ej: user_id)
def create_access_token(data: dict):
    to_encode = data.copy()
    # Define cuándo expira el token
    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    # Agrega la expiración al payload
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

# Decodifica el token y obtiene el user_id (campo "sub")
def decode_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None