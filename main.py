from flask import Flask, request, jsonify
import os
import datetime
import openai

app = Flask(__name__)

@app.route("/create_folder", methods=["POST"])
def create_folder():
    data = request.json
    folder_name = data.get("folder_name", "nola")
    path = os.path.join(os.getcwd(), folder_name)

    if not os.path.exists(path):
        os.makedirs(path)
        return jsonify({"status": "success", "message": f"Folder '{folder_name}' created."})
    else:
        return jsonify({"status": "exists", "message": f"Folder '{folder_name}' already exists."})

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "alive", "time": datetime.datetime.now().isoformat()})

@app.route("/command", methods=["POST"])
def command():
    data = request.json
    cmd = data.get("command", "(пусто)")
    response = f"Команда получена: {cmd}"
    return jsonify({"response": response})

@app.route("/think", methods=["POST"])
def think():
    data = request.json
    prompt = data.get("prompt", "Пусто")

    openai.api_key = "sk-..."  # Вставь свой ключ

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({"response": reply})
    except Exception as e:
        print("Ошибка мышления:", e)
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)