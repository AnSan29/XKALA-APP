# XKALA - MVP Sistema de Control de Ingreso de Personal 

## 📌 Descripción

Este proyecto es un MVP desarrollado con FastAPI que permite registrar
el ingreso y salida de empleados en una empresa de construcción,
incluyendo validación de EPP (Elementos de Protección Personal),
geolocalización e identificación por IP.

------------------------------------------------------------------------

## 🧱 Tecnologías

-   Backend: FastAPI (Python)
-   Base de datos: MySQL
-   ORM: SQLAlchemy
-   Autenticación: JWT
-   Seguridad: Bcrypt

------------------------------------------------------------------------

## 🔐 Funcionalidades principales

### 👤 Usuarios

-   Registro de empleados
-   Validación de datos con Pydantic
-   Contraseñas hasheadas

### 🔑 Autenticación

-   Login con documento + contraseña
-   Generación de token JWT
-   Protección de rutas

### 🟢 Registro de entrada

-   Guarda:
    -   Hora
    -   Ubicación (lat/lng)
    -   IP
    -   Checklist de EPP
-   Validación: solo una entrada por día

### 🔴 Registro de salida

-   Cierra turno
-   Guarda:
    -   Hora de salida
    -   Ubicación
    -   IP

------------------------------------------------------------------------

## 📍 Trazabilidad

El sistema registra: - Coordenadas exactas - Dirección IP - Uso de EPP

Esto permite auditoría y control laboral real.

------------------------------------------------------------------------

## 🗄️ Base de datos

Normalizada hasta 3FN: - usuarios - registros - registro_epp -
tipos_documento - eps - arl - cargos

------------------------------------------------------------------------

## 🌱 Seeders

Incluye script para cargar datos iniciales: - Tipos de documento - EPS -
ARL - Cargos

------------------------------------------------------------------------

## 🔐 Seguridad implementada

-   Hash de contraseñas (bcrypt)
-   Tokens JWT con expiración
-   Validación de usuario autenticado
-   Protección de endpoints

------------------------------------------------------------------------

## ⚙️ Configuración (.env)

DATABASE_URL=... SECRET_KEY=... ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

------------------------------------------------------------------------

## ▶️ Ejecución

``` bash
uvicorn main:app --reload
```

------------------------------------------------------------------------

## 🧪 Endpoints principales

### Login

POST /auth/login

### Crear usuario

POST /usuarios/

### Entrada

POST /registros/entrada

### Salida

POST /registros/salida

------------------------------------------------------------------------

## 🧠 Arquitectura

-   routes → endpoints
-   services → lógica de negocio
-   models → base de datos
-   schemas → validación
-   core → seguridad y config

------------------------------------------------------------------------

## 📌 Estado del proyecto

✅ MVP funcional completo\
🔜 Listo para frontend (Angular)\
🔜 Escalable a producción

------------------------------------------------------------------------

## 💡 Nota final

Este proyecto no es un CRUD simple. Implementa lógica real de negocio,
seguridad básica y trazabilidad, lo que lo hace apto como base para un
producto real.

------------------------------------------------------------------------

Autor: Andrés Santoyo
