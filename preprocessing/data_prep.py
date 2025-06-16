import pandas as pd

def prepare_symptom_data(path):
    df = pd.read_csv(path)

    print(df.columns)
    #Gather all unique symptoms
    symptoms = set()
    for col in df.columns[1:]: #skip 'disease'
        symptoms.update(df[col].dropna().unique())
    symptoms = sorted(list(symptoms))

    print(df.columns)
    print(symptoms)

prepare_symptom_data("/home/abhaytiwari/Projects/SmartHealthAI/data/DiseaseAndSymptoms.csv")

