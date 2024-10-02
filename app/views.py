from flask import request, jsonify, render_template
from app import app, db
from app.models import Item

# Dummy user credentials for demonstration
VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

@app.route('/login', methods=['POST'])
def login():
    data = request.json  # Expecting JSON data from React
    username = data.get('username')
    password = data.get('password')

    # Check credentials
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return jsonify({"message": "Login successful"}), 200  # Success response
    else:
        return jsonify({"message": "Invalid credentials"}), 401  # Error response
    
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()  # Retrieve all items from the database
    items_data = [{'id': item.id, 'value': item.value} for item in items]  # Format data

    # Debug: Print the item data to ensure values are correct
    print("Items Data:", items_data)

    return jsonify({'items': items_data})


@app.route('/calculate_percentages', methods=['POST'])
def calculate_percentages():
    data = request.json  # Expecting JSON data from the frontend
    numerical_values = data.get('numerical_values', [])
    
    # Get all items from the database
    items = Item.query.all()

    # Prepare a list of percentages
    percentages = []

    # Calculate percentages based on input numerical values
    for i in range(len(items)):
        if i < len(numerical_values) and numerical_values[i] is not None:
            try:
                input_value = float(numerical_values[i])
                item_value = float(items[i].value)
                percentage = (input_value / item_value) * 100
                percentages.append(round(percentage, 2))
            except (ValueError, ZeroDivisionError):
                percentages.append(None)  # Handle cases like division by zero or invalid inputs
        else:
            percentages.append(None)  # If no input, keep N/A

    # Return the result as JSON
    return jsonify({'percentages': percentages})

# Optional: If you need to enable CORS
from flask_cors import CORS

CORS(app)  # Enable CORS for all routes

