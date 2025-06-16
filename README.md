## 🔌 Flask API for SmartHealthAI

The project includes a Flask API that takes a list of symptoms and returns the predicted disease along with suggested precautions.

### 🔁 Endpoint

**POST** `/predict`

#### 🔧 Input (JSON)

```json
{
  "symptoms": ["itching", "skin_rash", "coughing_sneezing"]
}
```

#### Output(JSON)

```json
{
  "disease": "Fungal infection",
  "precautions": [
    "bath twice",
    "use detol or neem in bathing water",
    "keep infected area dry",
    "use clean cloths"
  ]
}
```




