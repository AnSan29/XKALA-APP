from pydantic import BaseModel, EmailStr

# Esquema para crear un usuario
class UsuarioCreate(BaseModel):
    nombres: str
    apellidos: str
    tipo_documento_id: int # FK al tipo de documento
    documento: str
     # Datos opcionales (pueden venir o no)
    grupo_sanguineo: str | None = None
    eps_id: int | None = None
    arl_id: int | None = None
    cargo_id: int | None = None
    telefono: str | None = None
    # Email validado automáticamente por Pydantic
    email: EmailStr | None = None
     # Contraseña en texto plano (luego se hashea en el backend)
    password: str