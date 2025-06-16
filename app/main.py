from flask import Flask, request, jsonify
import pickle
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(".."))

app = Flask(__name__)

model = pickle.load(open("models/symptom_model.pkl", "rb"))
symptopm_list = pickle.load(open("models/symptom_list.pkl", "rb"))

prec_df = pd.read_csv("data/disease_precaution.csv")

@app.route("/")
def home():
    return "SmartHealthAI is up and running 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    symptoms_input = request.json.get("symptoms", [])

    input_vector = [1 if s in symptoms_input else 0 for s in symptopm_list]

    disease = model.predict([input_vector])[0]

    precautions = prec_df[prec_df['Disease'].str.lower() == disease.lower()]
    if not precautions.empty:
        precaution_list = precautions.iloc[0, 1:].dropna().tolist()
    else:
        precaution_list = ["No precautions found"]

    return jsonify({
        "disease": disease,
        "precautions": precaution_list
    })

if __name__ == "__main__":
    app.run(debug=True)
