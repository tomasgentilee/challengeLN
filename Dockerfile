# Imagen base oficial de Python
FROM python:3.12.10-slim

# Variables de entorno para que Django no genere archivos .pyc y loguee en consola
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias para mysqlclient
RUN apt-get update \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements.txt y luego instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código del proyecto
COPY . .

# Exponer el puerto 8000 para acceder a Django
EXPOSE 8000

# Comando por defecto: levantar el servidor de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
