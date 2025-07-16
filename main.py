from flask import Flask, request, jsonify
from validator import validate_data
from auth import authorize
from processor import process_large_data

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def receive_data():
    token = request.headers.get('Authorization')

    if not authorize(token):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()

    is_valid, errors = validate_data(data)
    if not is_valid:
        return jsonify({"validation_errors": errors}), 400

    processed_data = process_large_data(data)
    return jsonify({"status": "success", "processed": processed_data}), 200

if __name__ == '__main__':
    app.run(debug=True)
