from flask import Flask, jsonify
try:
    from monitor import get_system_info
except ImportError:
    raise ImportError("The 'monitor.py' file is missing or not in the same directory as 'api.py'. Ensure it exists and contains the 'get_system_info' function.")

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    """
    Retourne les infos système collectées par monitor.py
    """
    data = get_system_info()
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
