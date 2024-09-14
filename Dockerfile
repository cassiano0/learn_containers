# Usar uma imagem Python oficial
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo requirements para o container
COPY requirements.txt requirements.txt

# Instalar as dependências Python
RUN pip install -r requirements.txt

# Copiar todo o código da aplicação para o container
COPY . .

# Expor a porta onde o Flask vai rodar
EXPOSE 80

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
