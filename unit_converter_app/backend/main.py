from flask import Flask, jsonify, request
from flask_cors import CORS

length_factors = {
    'millimeter': 0.001, 'mm': 0.001,
    'centimeter': 0.01, 'cm': 0.01,
    'meter': 1.0, 'm': 1.0,
    'kilometer': 1000.0, 'km': 1000.0,
    'inch': 0.0254, 'in': 0.0254,
    'foot': 0.3048, 'ft': 0.3048,
    'yard': 0.9144, 'yd': 0.9144,
    'mile': 1609.34, 'mi': 1609.34,
}

weight_factors = {
    'milligram': 0.001, 'mg': 0.001,
    'gram': 1.0, 'g': 1.0,
    'kilogram': 1000.0, 'kg': 1000.0,
    'ounce': 28.3495, 'oz': 28.3495,
    'pound': 453.592, 'lb': 453.592,
}

def convert_length_or_weight(value, initial_unit, final_unit, factors):

    initial_unit = initial_unit.lower()
    final_unit = final_unit.lower()
    base_value = value * factors[initial_unit]
    final_value = base_value / factors[final_unit]
    return final_value

def convert_to_celsius(value, initial_unit):
    unit = initial_unit.lower()
    if unit in ['fahrenheit', 'f']:
        return (value - 32) * 5.0 / 9.0
    elif unit in ['kelvin', 'k']:
        return value - 273.15
    elif unit in ['celsius', 'c']:
        return value
    else:
        raise ValueError("Invalid temperature unit.")
    
def convert_from_celsius(value, final_unit):
    unit = final_unit.lower()
    if unit in ['celsius', 'c']:
        return value
    elif unit in ['fahrenheit', 'f']:
        return (value * 9.0 / 5.0) + 32
    elif unit in ['kelvin', 'k']:
        return value + 273.15
    else:
        raise ValueError("Invalid final temperature unit")
    
def convert_temperature(value, initial_unit, final_unit):
    base_temp = convert_to_celsius(value, initial_unit)
    final_temp = convert_from_celsius(base_temp, final_unit)
    return final_temp

valid_length_units = set(length_factors.keys())
valid_weight_units = set(weight_factors.keys())
valid_temp_units = {"celsius", "fahrenheit", "kelvin", "c", "f", "k"}

app = Flask(__name__)
CORS(app)

def return_error(message, status_code):
    return jsonify({'error': message}), status_code

def handle_conversion(request_form, unit_type, valid_units, conversion_function, type_factors=None):

    value_str = request_form.get('value')
    initial_unit = request_form.get('initial')
    final_unit = request_form.get('final')

    if not all([value_str, initial_unit, final_unit]):
        return return_error("Missing required form parameters: 'value', 'initial', 'final'", 400)
    
    try:
        value = float(value_str)
    except(ValueError, TypeError):
        return return_error("Invalid input for 'value'. Must be a number.", 400)
    
    if initial_unit.lower() not in valid_units or final_unit.lower() not in valid_units:
        return return_error(f"Invalid unit(s). Please use one of the supported {unit_type} units.", 400)
    
    if unit_type == "temperature":
        converted_value = conversion_function(value, initial_unit, final_unit)
    else:
        converted_value = conversion_function(value, initial_unit, final_unit, type_factors)

    return jsonify({
        'original_value': value,
        'original_unit': initial_unit,
        'converted_value': round(converted_value, 4),
        'converted_unit': final_unit
    })
    
@app.route('/', methods=['GET'])
def root():
    return jsonify({'message':'Nothing to see here.',
                    'suggestion': 'Interact with /convert/<unit_type>'})

@app.route('/convert/length', methods=['POST'])
def convert_length_endpoint():
    return handle_conversion(request.form, 'length', valid_length_units, convert_length_or_weight, length_factors)

@app.route('/convert/weight', methods=['POST'])
def convert_weight_endpoint():
    return handle_conversion(request.form, 'weight', valid_weight_units, convert_length_or_weight, weight_factors)

@app.route('/convert/temp', methods=['POST'])
def convert_temp_endpoint():
    return handle_conversion(request.form, 'temperature', valid_temp_units, convert_temperature)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0') 
