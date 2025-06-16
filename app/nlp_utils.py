from transformers import pipeline

# Load once during server startup
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def extract_symptoms(text, known_symptoms, threshold=0.4):
    # known_symptoms: list of all 132 model symptoms
    result = classifier(text, known_symptoms, multi_label=True)

    # Pick only those symptoms where score > threshold
    predicted = [
        label for label, score in zip(result["labels"], result["scores"])
        if score > threshold
    ]

    return predicted
