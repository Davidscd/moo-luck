# Moo Luck

Moo Luck es un prototipo de gestion ganadera con:

- Frontend estatico en `Frontend/mooluck_website_green.html`.
- Backend Django REST Framework en `Backend/`.
- Base de datos PostgreSQL en Neon mediante `Backend/.env`.
- Cuentas personales de productores/gestores para administrar sus propias fincas.

## Modelo de uso

El flujo esperado es:

1. El productor crea una cuenta o inicia sesion.
2. Agrega una o varias fincas propias.
3. Registra manualmente el ganado de cada finca.
4. Registra produccion, eventos sanitarios y movimientos financieros.
5. El dashboard calcula alertas y resumen operativo con los datos de esa cuenta.

El frontend guarda la sesion en `localStorage` y usa un token Bearer devuelto por `/api/v1/usuarios/login/`. El backend guarda los tokens hasheados y filtra fincas, animales, produccion, salud y finanzas por propietario autenticado.

Ejemplo de consumo de API autenticada:

```http
Authorization: Bearer TU_TOKEN
```

Nota: para produccion real todavia conviene reemplazar el hash SHA-256 de password por el sistema nativo de Django o Argon2/bcrypt, agregar expiracion/rotacion de tokens y configurar permisos por rol con mas detalle.

## Ejecutar localmente

Desde la raiz del proyecto:

```powershell
Backend\venv\Scripts\python.exe Backend\manage.py runserver 0.0.0.0:8000
```

En otra terminal:

```powershell
Backend\venv\Scripts\python.exe -m http.server 5173 --bind 0.0.0.0 --directory Frontend
```

En el PC:

```text
http://127.0.0.1:5173/mooluck_website_green.html
```

En un celular conectado al mismo WiFi, usa la IP local del PC:

```text
http://TU_IP_LOCAL:5173/mooluck_website_green.html
```

La API local queda en:

```text
http://TU_IP_LOCAL:8000/api/v1/
```

## Configuracion local

Copia `Backend/.env.example` a `Backend/.env` y configura:

```env
DATABASE_URL=postgresql://...
SECRET_KEY=...
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0,TU_IP_LOCAL
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173,http://TU_IP_LOCAL:5173
```

Nunca subas `Backend/.env` a GitHub.

## Trabajo colaborativo

Cada colaborador debe:

1. Clonar el repositorio.
2. Crear su propio `Backend/.env`.
3. Crear o activar `Backend/venv`.
4. Instalar dependencias con `pip install -r Backend/requirements.txt`.
5. Ejecutar migraciones con `python Backend/manage.py migrate --fake-initial` si la base ya tiene tablas.
6. Levantar backend y frontend localmente.

## GitHub Pages

GitHub Pages puede servir el frontend estatico, pero no puede ejecutar Django.

Para usar GitHub Pages de forma real necesitas:

- Frontend publicado en GitHub Pages.
- Backend Django desplegado en un servicio con HTTPS, por ejemplo Render, Railway, Fly.io o similar.
- Neon como base de datos.
- Configurar el campo "Conexion API" del frontend con la URL publica del backend.

No es seguro conectar Neon directamente desde el navegador porque expondria credenciales de base de datos.

## Proximo paso recomendado

Para trabajo colaborativo y acceso desde cualquier dispositivo:

1. Desplegar Django en Render/Railway/Fly.io.
2. Configurar variables de entorno del backend en ese servicio.
3. Agregar la URL del frontend de GitHub Pages a `CORS_ALLOWED_ORIGINS`.
4. Publicar el frontend en GitHub Pages.
5. Usar la URL HTTPS del backend en el campo "Conexion API".
