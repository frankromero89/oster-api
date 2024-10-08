# Dockerfile
FROM python:3.11-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar el archivo requirements.txt y luego instalar las dependencias
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el contenido del proyecto al contenedor
COPY . .

# Comando para iniciar la aplicación con uvicorn, esperando primero a MySQL
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
