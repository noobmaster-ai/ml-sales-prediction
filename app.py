from flask import Flask, request, jsonify, render_template_string
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# HTML Template for input form
HTML_FORM = """
<!doctype html>
<title>Sales Predictor</title>
<h2>Sales Prediction</h2>
<form method="post" action="/predict_web">
  <label for="features">Marketing Spend:</label><br><br>
  <input type="text" name="features" size="50"><br><br>
  <input type="submit" value="Predict">
</form>
{% if prediction is not none %}
  <h3>Predicted Sales: {{ prediction }}</h3>
{% endif %}
"""

@app.route('/')
def home():
    return render_template_string(HTML_FORM, prediction=None)

@app.route('/predict_web', methods=['POST'])
def predict_web():
    try:
        feature_input = request.form['features']
        features = np.array([float(x.strip()) for x in feature_input.split(',')]).reshape(1, -1)
        prediction = model.predict(features)[0]
        return render_template_string(HTML_FORM, prediction=round(prediction,2))
    except Exception as e:
        return f"Error processing input: {e}"

@app.route('/predict', methods=['POST'])
def predict_api():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'predicted_sales': round(prediction[0], 2)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
