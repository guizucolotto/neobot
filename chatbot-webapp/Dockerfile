# Usando imagem do OpenJDK para rodar o WebApp
FROM openjdk:11

# Diretório de trabalho
WORKDIR /app

# Copiando o arquivo JAR do WebApp
COPY target/chatbot-webapp.jar .

# Expondo a porta do WebApp
EXPOSE 8080

# Comando para rodar o WebApp
CMD ["java", "-jar", "chatbot-webapp.jar"]
