from flask import Flask, request, jsonify
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)

# Definir o modelo Llama
template = """
    Responda à pergunta abaixo.

    Aqui está o histórico da conversa: {context}

    Pergunta: {question}

    Resposta:
"""

model = OllamaLLM(model='llama3.2-vision')  # ou 'llama3'

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    context = data.get('context', "")
    question = data.get('question', "")

    result = chain.invoke({'context': context, 'question': question})
    context += f"\nVocê: {question}\nIA: {result}"

    return jsonify({'response': result, 'context': context})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

