
from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import pickle

# Load the trained model (Ensure you save your model using pickle)
model_path = 'football_model.pkl'
model = pickle.load(open(model_path, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Homepage with optional input form

@app.route('/predict', methods=['POST'])
def predict():
    # API endpoint to predict 'Overall' rating or select a team based on input attributes.
    try:
        data = request.get_json()  # Expecting JSON input
        df = pd.DataFrame(data)    # Convert input to DataFrame

        # Ensure the input DataFrame has the correct format (columns in the right order)
        prediction = model.predict(df)  # Predict using the loaded model
        
        # Return predictions as JSON response
        return jsonify({"predictions": prediction.tolist()})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
