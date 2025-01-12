from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the model and scaler
with open("model_007.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler_007.pkl", "rb") as f:
    scaler = pickle.load(f)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse JSON data
        data = request.json
        features = data.get('features')  # Extract features from JSON
        if not features or not isinstance(features, list):
            return jsonify({'error': 'Invalid input format. Expected a list of features.'}), 400
        
        # Preprocess input and predict
        features = np.array(features).reshape(1, -1)  # Convert to 2D array
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)
        
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
