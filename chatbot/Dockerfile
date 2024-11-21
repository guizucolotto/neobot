# Usando imagem oficial do Python
FROM python:3.9

# Definindo diretório de trabalho
WORKDIR /app

# Instalando dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiando o código do chatbot para o contêiner
COPY . .

# Expondo a porta para a API
EXPOSE 5000

# Comando para rodar o chatbot
CMD ["python", "app.py"]
