# PeopleFlow - Backend Django Challenge

API Backend construida con **Django + Django REST Framework**, contenerizada con **Docker**, utilizando **MySQL** como base de datos y **JWT Authentication** para el login de usuarios.

Este proyecto fue desarrollado como parte de un challenge técnico para un puesto de Backend Developer Jr+/Ssr.

---

## 🚀 Funcionalidades

- Operaciones CRUD para **Empleados** (nombre, apellido, email, puesto, salario, fecha de ingreso).
- **Autenticación JWT** con `djangorestframework-simplejwt`.
- Acciones personalizadas:
  - Actualizar todos los salarios por porcentaje.
  - Generar y enviar un reporte semanal de salarios (simulado vía consola).
- Paginación y búsqueda de empleados por puesto.
- Entorno completamente dockerizado (Django + MySQL).

---

## 🛠️ Requisitos

- Docker y Docker Compose instalados  
- Python 3.12 (solo necesario si corres en local sin Docker)  
- Git  

---

## ⚙️ Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/<tu-usuario>/peopleflow-django.git
cd peopleflow-django


Project setup
Dentro del ambiente virtual env correr la siguiente linea para instalar todas las dependencias:

pip install -r requirements.txt

Crea un archivo .env (solo debe llamarse .env) con lo siguiente:

SECRET_KEY='tu_secret_key'
DEBUG='True'
DB_NAME='db_name'
DB_USER='db_user'
DB_PASSWORD='db_password'
DB_HOST='db_host'
PORT='port'


Para levantar la imagen de docker correr

docker run -p 8000:8000 peopleflow-django

| Método | Endpoint                          | Descripción                          |
| ------ | --------------------------------- | ------------------------------------ |
| GET    | `/api/employees/`                 | Listar todos los empleados           |
| GET    | `/api/employees/{id}/`            | Obtener un empleado por ID           |
| POST   | `/api/employees/`                 | Crear un nuevo empleado              |
| PUT    | `/api/employees/{id}/`            | Editar empleado por ID               |
| DELETE | `/api/employees/{id}/`            | Eliminar empleado                    |
| POST   | `/api/employees/update-salaries/` | Actualizar todos los salarios en %   |
| POST   | `/api/employees/send-report/`     | Generar y enviar reporte de salarios |
