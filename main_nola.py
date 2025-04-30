import os
import openai
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from nola_pulse import NolaPulse
from nola_agent import NolaAgent

# Загружаем переменные окружения
load_dotenv()

# Инициализируем клиента OpenAI
openai_client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Flask-приложение
app = Flask(__name__)

# Пульс Нолы
pulse = NolaPulse(interval_seconds=60)
pulse.start()
print("NolaPulse был запущен")

# Агент Нолы
agent = NolaAgent()
print("NolaAgent инициализирован")

# Эндпоинт команд
@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()
    cmd = data.get("command", "")
    response = agent.execute(cmd)
    return jsonify({"response": response})

# Эндпоинт мышления
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

# Статус
@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "status": "alive",
        "time": str(os.popen("date").read().strip())
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)