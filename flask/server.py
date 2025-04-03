from flask import Flask, jsonify, request

sample_dict = {
    "artie-wong": {
        "name": "Artie Wong",
        "age": 13,
        "city": "Cambridge",
        "favoriteSubject": "Computer Science"
    },
    "jayden-jimenez": {
        "name": "Jayden Jimenez",
        "age": 13,
        "city": "Cambridge",
        "favoriteSubject": "Computer Science"
},}

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def handle_request():
    data = request.json
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    return jsonify({"message": "Data received", "data": data}), 200

@app.route('/get-dict', methods=['GET'])
def get_dict():
    return jsonify(sample_dict), 200

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)