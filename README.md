# PeopleFlow - Backend Django Challenge

API Backend construida con **Django + Django REST Framework**, contenerizada con **Docker**, utilizando **MySQL** como base de datos y **JWT Authentication** para el login de usuarios.

---

## Funcionalidades

- Operaciones CRUD para **Empleados** (nombre, apellido, email, puesto, salario, fecha de ingreso).
- **Autenticación JWT** con `djangorestframework-simplejwt`.
- Acciones personalizadas:
  - Generar y enviar un reporte semanal de salarios (simulado vía consola).
- Paginación y búsqueda de empleados por puesto.
- Entorno completamente dockerizado (Django + MySQL).

---

## Requisitos

- Docker y Docker Compose instalados  
- Python 3.12 (solo necesario si corres en local sin Docker)  
- Git  

---

## Instalación en entorno local (sin Docker)

### 1. Clonar el repositorio
bash

[git clone https://github.com/<tu-usuario>/challengeLN.git](https://github.com/tomasgentilee/challengeLN.git)

cd challengeLN


### 2. Crear y activar un entorno virtual
python -m venv venv

source venv/bin/activate   # Linux/Mac

venv\Scripts\activate      # Windows

### 3. Instalar dependencias
pip install -r requirements.txt

### 4. Configuración de variables de entorno
Crear un archivo .env en la raíz del proyecto (solo debe llamarse .env) con el siguiente contenido:

SECRET_KEY='tu_secret_key'

DEBUG='True'

DB_NAME='db_name'

DB_USER='db_user'

DB_PASSWORD='db_password'

DB_HOST='db_host'

PORT='port'

### 5. Aplicar migraciones
python manage.py migrate

### 6. Levantar el servidor
python manage.py runserver

---

## Instalación con Docker

### 1. Construir la imagen
docker build -t peopleflow-django .

### 2. Levantar el contenedor
docker run -p 8000:8000 peopleflow-django

### 3. (Opcional) Usando docker-compose
docker-compose up --build

Configuración de la base de datos

### Aplicar migraciones dentro del contenedor:
docker-compose exec web python manage.py migrate
