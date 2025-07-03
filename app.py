from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load model and encoder
model = joblib.load("weather_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

app = Flask(__name__)

# Expected input features
FEATURES = ["precipitation", "temp_max", "temp_min", "wind"]

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Validate all required features are present
    missing = [f for f in FEATURES if f not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {missing}"}), 400

    try:
        input_df = pd.DataFrame([{f: float(data[f]) for f in FEATURES}])
        pred_encoded = model.predict(input_df)[0]
        pred_label = label_encoder.inverse_transform([pred_encoded])[0]
        return jsonify({"prediction": pred_label})
    except ValueError:
        return jsonify({"error": "Invalid input types. Expecting numeric values."}), 400

if __name__ == "__main__":
    app.run(debug=True)
