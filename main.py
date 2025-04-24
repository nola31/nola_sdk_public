from flask import Flask, request, jsonify
import os
import datetime

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
