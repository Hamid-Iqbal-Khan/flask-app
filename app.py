from flask import Flask, jsonify
import json

app = Flask(__name__)

# File path where data is stored
DATA_FILE = 'data.json'

def read_data_from_file():
    """Function to read data from a JSON file"""
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {"error": "Data file not found"}
    except json.JSONDecodeError:
        return {"error": "Error in decoding JSON data"}

@app.route('/api', methods=['GET'])
def api_route():
    """API route to return JSON data"""
    data = read_data_from_file()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
