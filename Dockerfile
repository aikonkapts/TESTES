# Usa uma imagem base com Python
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os ficheiros da aplicação para o container
COPY app.py .
COPY login.py .

# Instala o Flask
RUN apt-get update \
    && apt-get install -y python3-tk \
    && pip install flask \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Expõe a porta
EXPOSE 5000

# Comando para correr a app
CMD ["python", "login.py"]
