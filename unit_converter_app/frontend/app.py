from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

BACKEND_URL = os.environ.get('BACKEND_URL', 'http://localhost:5000')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    unit_type = request.form.get('unit_type')
    value = request.form.get('value')
    from_unit = request.form.get('from_unit')
    to_unit = request.form.get('to_unit')
    
    if not all([unit_type, value, from_unit, to_unit]):
        return jsonify({'error': 'All fields are required'}), 400
    
    try:
        # Forward the request to the backend API
        response = requests.post(
            f"{BACKEND_URL}/convert/{unit_type}",
            data={
                'value': value,
                'initial': from_unit,
                'final': to_unit
            }
        )
        
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Could not connect to the conversion service: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)