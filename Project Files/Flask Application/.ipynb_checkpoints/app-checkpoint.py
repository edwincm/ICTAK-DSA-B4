from flask import Flask, request, jsonify
from joblib import load
import numpy as np
import pandas as pd

# Load the saved model
model = load('best_rf_model.joblib')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML form

@app.route('/predict', methods=['POST'])
def predict():
    # API endpoint to predict 'Overall' rating based on input attributes
    try:
        data = request.get_json()  # Expecting JSON input
        features = np.array(data['features']).reshape(1, -1)  # Reshape for a single prediction

        # Validate input dimensions
        if features.shape[1] != model.n_features_in_:
            return jsonify({'error': f'Expected {model.n_features_in_} features, but got {features.shape[1]}'}), 400

        # Make the prediction using the loaded model
        prediction = model.predict(features)[0]  # Get the first element (since it's a single prediction)

        # Return the prediction as a JSON response
        response = {
            'prediction': prediction
        }
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)