# 🐄 Backend Ganadería — Django REST Framework + Neon PostgreSQL

## Estructura del proyecto

```
ganaderia_backend/
├── manage.py
├── requirements.txt
├── .env.example
├── ganaderia/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── apps/
    ├── fincas/
    ├── usuarios/
    ├── animales/
    ├── producciones/
    ├── eventos_sanitarios/
    ├── pesajes/
    ├── partos/
    └── finanzas/
```

---

## ⚙️ Instalación paso a paso

### 1. Crear y activar entorno virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno
```bash
# Copia el archivo de ejemplo
cp .env.example .env
```

Abre `.env` y pega tu connection string de Neon:
```
DATABASE_URL=postgresql://usuario:password@ep-xxxxx.us-east-2.aws.neon.tech/nombre_db
SECRET_KEY=una-clave-secreta-larga-y-aleatoria
DEBUG=True
```

> 💡 Encuentra tu connection string en Neon → tu proyecto → **Connection Details**

### 4. Ejecutar migraciones
```bash
# Como las tablas ya existen en Neon, solo marca las migraciones como aplicadas
python manage.py migrate --fake-initial

# O si quieres que Django cree las tablas desde cero en una BD vacía:
python manage.py migrate
```

### 5. Crear superusuario de Django Admin (opcional)
```bash
python manage.py createsuperuser
```

### 6. Correr el servidor
```bash
python manage.py runserver
```

Abre en el navegador: **http://localhost:8000/api/v1/**

---

## 📡 Endpoints disponibles

| Recurso              | URL                                  | Métodos              |
|----------------------|--------------------------------------|----------------------|
| Fincas               | `/api/v1/fincas/`                    | GET, POST            |
| Finca detalle        | `/api/v1/fincas/{id}/`               | GET, PUT, PATCH, DELETE |
| Usuarios             | `/api/v1/usuarios/`                  | GET, POST            |
| Animales             | `/api/v1/animales/`                  | GET, POST            |
| Producciones         | `/api/v1/producciones/`              | GET, POST            |
| Resumen producción   | `/api/v1/producciones/resumen/`      | GET                  |
| Eventos sanitarios   | `/api/v1/eventos-sanitarios/`        | GET, POST            |
| Próximos eventos     | `/api/v1/eventos-sanitarios/proximos/` | GET                |
| Pesajes              | `/api/v1/pesajes/`                   | GET, POST            |
| Partos               | `/api/v1/partos/`                    | GET, POST            |
| Categorías gasto     | `/api/v1/finanzas/categorias/`       | GET, POST            |
| Transacciones        | `/api/v1/finanzas/transacciones/`    | GET, POST            |
| Balance financiero   | `/api/v1/finanzas/transacciones/balance/` | GET             |

---

## 🔍 Filtros y búsqueda

```bash
# Animales de una finca específica
GET /api/v1/animales/?finca=<uuid>

# Animales hembras activas
GET /api/v1/animales/?sexo=hembra&estado=activo

# Producción de un animal en un rango de fechas
GET /api/v1/producciones/?animal=<uuid>&fecha_desde=2024-01-01&fecha_hasta=2024-12-31

# Eventos sanitarios próximos (30 días)
GET /api/v1/eventos-sanitarios/proximos/

# Balance financiero de una finca
GET /api/v1/finanzas/transacciones/balance/?finca=<uuid>

# Búsqueda de animales por nombre o código
GET /api/v1/animales/?search=vaca01
```

---

## 🛠️ Panel de administración

Django Admin disponible en: **http://localhost:8000/admin/**
(requiere haber creado un superusuario)

---

## 🚀 Despliegue en producción

Recuerda cambiar en `.env`:
```
DEBUG=False
ALLOWED_HOSTS=tu-dominio.com
SECRET_KEY=clave-muy-larga-y-segura
```
