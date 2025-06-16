from flask import Flask, request, jsonify, render_template
from forms import SymptomForm
from nlp_utils import extract_symptoms
import os
import pickle
import pandas as pd
from dotenv import load_dotenv
load_dotenv()



app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'fallback-key')

model = pickle.load(open("models/symptom_model.pkl", "rb"))
symptom_list = pickle.load(open("models/symptom_list.pkl", "rb"))

prec_df = pd.read_csv("data/disease_precaution.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    form = SymptomForm()
    result = None

    if form.validate_on_submit():
        desc = form.description.data
        symptoms_input = extract_symptoms(desc, symptom_list)

        input_vector = [1 if s in symptoms_input else 0 for s in symptom_list]
        disease = model.predict([input_vector])[0]

        precautions = prec_df[prec_df['Disease'].str.lower() == disease.lower()]
        precaution_list = precautions.iloc[0, 1:].dropna().tolist() if not precautions.empty else ["No data"]

        result = {"disease": disease, "precautions": precaution_list}

    return render_template("index.html", form=form, result=result)



if __name__ == "__main__":
    app.run(debug=True)
