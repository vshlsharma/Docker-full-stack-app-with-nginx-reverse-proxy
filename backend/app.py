from flask import Flask, jsonify
import socket

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return f"Hello from Backend! Host: {socket.gethostname()}"

# API route
@app.route('/api')
def api():
    data = {
        "message": "This is backend API response",
        "hostname": socket.gethostname()
    }
    return jsonify(data)

# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
