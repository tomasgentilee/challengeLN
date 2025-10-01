Sistema de gestión para PeopleFlow▶

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

