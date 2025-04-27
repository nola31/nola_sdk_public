import openai
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify

# Загружаем переменные окружения из .env файла
load_dotenv()

# Подключаем ключ OpenAI из окружения
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()
    cmd = data.get("command", "")
    return jsonify({"response": f"say hello: {cmd}"})

@app.route("/think", methods=["POST"])
def think():
    data = request.get_json()
    prompt = data.get("prompt", "")

    try:
        completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        response_text = completion.choices[0].text.strip()
        return jsonify({"response": response_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)