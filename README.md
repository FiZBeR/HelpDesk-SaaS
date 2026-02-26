# 🚀 HelpDesk SaaS API - Sistema de Gestión de Tickets

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Django](https://img.shields.io/badge/Django-REST_Framework-092E20.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon_Tech-336791.svg)
![JWT](https://img.shields.io/badge/Auth-JWT-black.svg)
![Render](https://img.shields.io/badge/Deployed_on-Render-purple.svg)

## 📌 Descripción General
API RESTful robusta y escalable construida para un sistema de HelpDesk SaaS. Permite la gestión completa del ciclo de vida de los tickets de soporte, desde la creación hasta la resolución, integrando un sistema de roles de usuario, autenticación segura y documentación interactiva.

**URL de Producción (Swagger/OpenAPI):** [https://help-desk-api-p3yx.onrender.com/docs/](https://help-desk-api-p3yx.onrender.com/docs/)

## 🏗️ Decisiones Arquitectónicas

Para este proyecto se priorizó la seguridad, la escalabilidad y las mejores prácticas de despliegue en la nube:

* **Autenticación (SimpleJWT):** Implementación de tokens de acceso y refresco (JSON Web Tokens) para mantener sesiones seguras sin estado (stateless) entre el cliente React y el servidor Django.
* **Base de Datos Serverless (Neon Tech):** Migración de SQLite a PostgreSQL alojado en Neon para garantizar concurrencia real, integridad de datos relacionales y escalabilidad en la nube (`sslmode=require`).
* **Gestión de Archivos Estáticos (Whitenoise):** Configuración de Whitenoise para servir los estáticos de la aplicación (como la interfaz de Swagger y el panel de Admin) directamente desde Gunicorn sin necesidad de configurar un proxy inverso como Nginx adicional.
* **Seguridad y Entornos:** Separación estricta de variables de entorno (`.env`) para `SECRET_KEY`, `DEBUG` y credenciales de base de datos, evitando la exposición de secretos en el control de versiones.

## 🛠️ Stack Tecnológico
* **Backend:** Django 5.x, Django REST Framework (DRF)
* **Base de Datos:** PostgreSQL (Neon Tech)
* **Autenticación:** djangorestframework-simplejwt
* **Documentación:** drf-yasg (Swagger UI)
* **Despliegue:** Render, Gunicorn, Whitenoise
* **Control de Versiones:** Git & GitHub

## 🚀 Instalación y Ejecución Local

Si deseas correr este proyecto en tu entorno de desarrollo, sigue estos pasos:

### 1. Clonar el repositorio y crear el entorno virtual

* git clone [https://github.com/FiZBeR/HelpDesk-SaaS.git](https://github.com/FiZBeR/HelpDesk-SaaS.git)
* cd HelpDesk-SaaS
* python -m venv venv
* source venv/bin/activate  # En Windows: venv\Scripts\activate

### 2. Instalar dependencias

* pip install -r requirements.txt

### 3. Configurar Variables de Entorno
Crea un archivo .env en la raíz del proyecto y añade las siguientes variables:

* ++DEBUG**=True
* **SECRET_KEY**=tu_clave_local_segura
* **DATABASE_URL**=postgres://usuario:password@host_local:5432/nombre_bd

### 4. Aplicar Migraciones y Crear Superusuario

* python manage.py migrate
* python manage.py createsuperuser

### 5. Ejecutar el Servidor

* python manage.py runserver
