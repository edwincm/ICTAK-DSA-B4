# Create a virtual environment and install all dependencies using:
# pip install -r requirements.txt

from flask import Flask, request, jsonify, render_template
from joblib import load
import numpy as np
import logging

# Initialize the Flask app
app = Flask(__name__)

# Load the saved model
try:
    model = load('static/best_rf_model.joblib')
    model_features = model.n_features_in_  # Number of features expected by the model
except Exception as e:
    raise RuntimeError(f"Failed to load the model. Error: {str(e)}")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML form

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse the JSON request
        data = request.get_json()
        if not data or 'features' not in data:
            logging.error("Invalid input: Missing 'features' key in the request data.")
            return jsonify({'error': "Invalid input: 'features' key is required."}), 400

        # Validate and reshape the features
        features = np.array(data['features'], dtype=float).reshape(1, -1)
        if features.shape[1] != model_features:
            logging.error(f"Feature count mismatch: Expected {model_features}, but got {features.shape[1]}.")
            return jsonify({'error': f"Expected {model_features} features, but got {features.shape[1]}"}), 400

        # Predict using the loaded model
        prediction = model.predict(features)[0]
        logging.info(f"Prediction successful. Features: {features}, Prediction: {prediction}")

        # Return the prediction as JSON
        return jsonify({'prediction': prediction})

    except Exception as e:
        logging.exception("An error occurred during prediction.")
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)