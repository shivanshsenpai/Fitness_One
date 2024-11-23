import subprocess
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow CORS for cross-origin requests

@app.route('/run-python')
def run_python():
    try:
        # Run the Python file and capture the output
        result = subprocess.run(['python', 'chat1.py'], capture_output=True, text=True)
        # Return the stdout result to the client
        return jsonify({'result': result.stdout})
    except Exception as e:
        # If there is an error, return the error message
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
