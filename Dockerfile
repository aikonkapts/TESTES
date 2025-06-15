# Usa uma imagem base com Python
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os ficheiros da aplicação para o container
COPY app.py .

# Instala o Flask
RUN pip install flask

# Expõe a porta
EXPOSE 5000

# Comando para correr a app
CMD ["python", "app.py"]
