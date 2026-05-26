# Moo Luck

Moo Luck es un prototipo de gestion ganadera con:

- Frontend estatico en `Frontend/mooluck_website_green.html`.
- Backend Django REST Framework en `Backend/`.
- Base de datos PostgreSQL en Neon mediante `Backend/.env`.

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
