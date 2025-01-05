# Usar uma imagem base Linux com suporte a Python
FROM python:3.9-slim

# Atualizar pacotes e instalar dependências necessárias para o Ollama
RUN apt-get update && apt-get install -y curl unzip

# Baixar e instalar o Ollama
RUN curl -L https://ollama.com/install.sh | bash

# Instalar dependências Python
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação Flask
COPY . /app

# Expor a porta para a aplicação Flask
EXPOSE 5000

# Comando para iniciar o Ollama e a aplicação Flask
CMD ["sh", "-c", "ollama serve & python app.py"]
