from flask import Flask, request, jsonify
from neo4j import GraphDatabase
import openai

# Configurações
app = Flask(__name__)
neo4j_driver = GraphDatabase.driver("bolt://neo4j:7687", auth=("neo4j", "password"))
openai.api_key = "your_openai_api_key"

# Função de busca e resposta usando RAG
def search_graph(query):
    with neo4j_driver.session() as session:
        result = session.run(query)
        return [record["name"] for record in result]  # Ajuste de acordo com o schema

def generate_response(question):
    documents = search_graph("MATCH (n) RETURN n.name")  # Ajuste o Cypher conforme necessário
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Documentos: {documents}\nPergunta: {question}\nResposta:",
        max_tokens=150
    )
    return response.choices[0].text.strip()

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get("question")
    answer = generate_response(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
