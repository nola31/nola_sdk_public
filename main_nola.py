import openai
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from nola_pulse import NolaPulse

# Загружаем переменные окружения из .env файла
load_dotenv()

# Создаём клиент OpenAI
openai_client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

app = Flask(__name__)

# Запускаем пульс
pulse = NolaPulse(interval_seconds=60)
pulse.start()
print("NolaPulse был запущен")

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
        response = openai_client.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        response_text = response.choices[0].message.content.strip()
        return jsonify({"response": response_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "status": "alive",
        "time": str(os.popen("date").read().strip())
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)