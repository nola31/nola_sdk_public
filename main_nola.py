main_nola.py

import os import threading import time from dotenv import load_dotenv from flask import Flask, request, jsonify import openai from nola_pulse import start_pulse

Загружаем переменные окружения

load_dotenv()

Создаём клиента OpenAI

openai_client = openai.OpenAI( api_key=os.getenv("OPENAI_API_KEY") )

app = Flask(name)

@app.route("/command", methods=["POST"]) def command(): data = request.get_json() cmd = data.get("command", "") return jsonify({"response": f"say hello: {cmd}"})

@app.route("/think", methods=["POST"]) def think(): data = request.get_json() prompt = data.get("prompt", "")

try:
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    response_text = response.choices[0].message.content.strip()
    return jsonify({"response": response_text})
except Exception as e:
    return jsonify({"error": str(e)}), 500

if name == "main": # Запускаем "пульс" в отдельном потоке threading.Thread(target=start_pulse, daemon=True).start() app.run(host="0.0.0.0", port=5000)

