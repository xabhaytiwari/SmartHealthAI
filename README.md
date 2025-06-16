
---

## 🧠 SmartHealthAI

An AI-powered personal health assistant that predicts diseases based on user-described symptoms and suggests appropriate precautions.

### 🚀 Features

* **Natural Language Symptom Input**: Users can describe symptoms in their own words using a secure form powered by Flask-WTF.
* **Transformer-Based Symptom Extraction**: Uses `facebook/bart-large-mnli` via Hugging Face Transformers to intelligently extract symptoms from user text (zero-shot classification).
* **Disease Prediction**: Predicts the most probable disease using a trained ML model.
* **Precaution Suggestion**: Returns top 3 precautions for the predicted condition.
* **Secure Flask Setup**: Uses environment variables to manage secrets like `SECRET_KEY` (not hardcoded).

### 🛠️ Technologies Used

* **Backend**: Python, Flask, Flask-WTF
* **NLP**: Hugging Face Transformers (`facebook/bart-large-mnli`)
* **ML**: scikit-learn (pickled model)
* **Data Handling**: pandas
* **Frontend**: HTML, CSS (basic)
* **Security**: `.env` for environment variables

---

Let me know if you'd like me to generate the full README file or add deployment instructions (like using Gunicorn or Heroku).
