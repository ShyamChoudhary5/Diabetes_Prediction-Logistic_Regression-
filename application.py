import pickle

from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)

classification_model = pickle.load(open(r"C:\Users\godar\OneDrive\Desktop\study material\Machine Learning\Regression\Logistic Regression\End to End project\Model\classification.pkl", 'rb'))
scaler_model = pickle.load(open(r"C:\Users\godar\OneDrive\Desktop\study material\Machine Learning\Regression\Logistic Regression\End to End project\Model\scale.pkl", 'rb'))

@application.route('/')
def index():
    return render_template('index.html')

def home():
    return render_template('index.html')

@application.route('/predict', methods=['POST'])

def predict():
    try:
        features = [
            float(request.form['Pregnancies']),
            float(request.form['Glucose']),
            float(request.form['BloodPressure']),
            float(request.form['SkinThickness']),
            float(request.form['Insulin']),
            float(request.form['BMI']),
            float(request.form['DiabetesPedigreeFunction']),
            float(request.form['Age'])
        ]
        
        final_features = np.array(features).reshape(1, -1)
        scaler = scaler_model.fit_transform(final_features)
        prediction = classification_model.predict(scaler)
        output = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
        
        return render_template('index.html', prediction_text=f'Prediction: {output}')
    except Exception as e:
        return f"Error: {str(e)}"



if __name__ == "__main__":
    application.run(host='0.0.0.0')