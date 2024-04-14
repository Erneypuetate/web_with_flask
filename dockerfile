# Usar la imagen base oficial de Python
FROM python:3.9-slim

RUN apt-get update \
    && apt-get install -y pkg-config \
                           libmariadb-dev-compat \
                           build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libmariadb-dev-compat \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install mysqlclient

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar el archivo de requisitos a la imagen
COPY requirements.txt requirements.txt

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el contenido del directorio actual al directorio de trabajo en la imagen
COPY . .

# Exponer el puerto 5000 para la aplicación Flask
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
