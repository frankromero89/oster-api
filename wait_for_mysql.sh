#!/bin/sh

# Esperar a que la base de datos MySQL esté lista
while ! nc -z db 3306; do
  echo "Esperando a que MySQL se inicie..."
  sleep 2
done

echo "MySQL está listo. Iniciando la aplicación..."
exec "$@"
