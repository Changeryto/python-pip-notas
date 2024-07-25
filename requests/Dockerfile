# Version instalada
FROM python:3.12.4

# Directorio de trabajo
WORKDIR /app
COPY requirements.txt /app/requirements.txt

# Dejar lisas las dependencias
RUN pip install -r /app/requirements.txt --no-cache-dir --upgrade

# Copiar todo el codigo a app
COPY . /app

# Encender el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
