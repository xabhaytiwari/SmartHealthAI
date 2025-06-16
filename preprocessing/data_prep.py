import pandas as pd

def prepare_symptom_data(path):
    df = pd.read_csv(path)

    # print(df.columns)
    # Gather all unique symptoms
    symptoms = set()
    for col in df.columns[1:]: #skip 'disease'
        symptoms.update(df[col].dropna().unique())
    symptoms = sorted(list(symptoms))

    # print(symptoms)

    def encode_symptoms(row):
        present = set(row.dropna().values)
        return [1 if s in present else 0 for s in symptoms]
    
    X = df.iloc[:, 1:].apply(encode_symptoms, axis=1, result_type='expand')
    X.columns = symptoms # Just names the columns of this new DataFrame
    y = df['Disease']

    return X, y, symptoms

