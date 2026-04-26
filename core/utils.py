from fastapi import Request

# Obtiene la IP del cliente que hace la petición
def get_client_ip(request: Request):
    # Intenta obtener la IP real desde el header (cuando hay proxy o servidor intermedio)
    forwarded = request.headers.get("X-Forwarded-For")
    # Si existe el header, puede traer varias IP separadas por coma
    if forwarded:
        return forwarded.split(",")[0]

    # Si no hay proxy, toma la IP directa del cliente
    return request.client.host