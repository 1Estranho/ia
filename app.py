from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def handle_post():
    # Obtém dados enviados no corpo da requisição
    data = request.get_json()
    if not data:
        return jsonify({"error": "Nenhum dado enviado"}), 400

    # Responde com uma mensagem baseada nos dados recebidos
    nome = data.get('nome', 'desconhecido')
    return jsonify({"mensagem": f"Olá, {nome}! Recebi seu POST com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)
