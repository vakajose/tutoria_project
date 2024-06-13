FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . .
# Copiar .env.example a .env
#RUN cp .env.example .env
# Instalar dependencias de desarrollo
RUN pip install -r requirements.txt

# Exponer el puerto en el que correrá la aplicación
EXPOSE 5000

# Establecer variables de entorno para desarrollo
ENV FLASK_DEBUG=true
ENV FLASK_RUN_PORT=5000

# Comando para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]
