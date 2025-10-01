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

### 1. Clonar el repositorio
bash

git clone https://github.com/tomasgentilee/challengeLN.git

cd challengeLN

---

## Instalación con Docker

### 1. Crear las variables de entorno
Crear un archivo .env en la raíz del proyecto (solo debe llamarse .env) con el siguiente contenido:

SECRET_KEY='django-insecure-$)m^7=i%k6%-%21!v3z#03_r2wvj&$6a5g4%fge=qz6hk)2-(='

DEBUG='True'

DB_NAME='peopleflow'

DB_USER='root'

DB_PASSWORD='rootpass'

DB_HOST='mysql_peopleflow'

PORT='3306'

### 2. Usando docker-compose
docker-compose up --build

---

## Instalación en entorno local (sin Docker)

### 1. Crear y activar un entorno virtual
python -m venv venv

source venv/bin/activate   # Linux/Mac

venv\Scripts\activate      # Windows

### 2. Instalar dependencias
pip install -r requirements.txt

### 3. Configuración de variables de entorno
Crear un archivo .env en la raíz del proyecto (solo debe llamarse .env) con el siguiente contenido:

SECRET_KEY='tu_secret_key'

DEBUG='True'

DB_NAME='db_name'

DB_USER='db_user'

DB_PASSWORD='db_password'

DB_HOST='db_host'

PORT='port'

### 4. Aplicar migraciones
python manage.py migrate

### 5. Levantar el servidor
python manage.py runserver

---

## Hacer consultas a la base de datos
En un cmd en la raíz del proyecto

docker-compose exec db mysql -u root -p

password: rootpass

USE peopleflow;

De esa forma ya estará usando la base de datos del proyecto