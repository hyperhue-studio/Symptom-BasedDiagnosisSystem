# Defining the library of symptoms and diagnoses
symptoms = ["fever", "cough", "sore_throat", "nasal_congestion"]

diagnosis = {
    "smallpox": [True, False, False, False],
    "flu": [True, True, True, True],
    "coronavirus": [True, True, False, True],
    "influenza": [True, True, False, False],
    "common cold": [False, True, True, True],
}

# Function that diagnoses based on symptoms
def make_diagnosis(symptoms):
    possible_diseases = []
    for disease, disease_symptoms in diagnosis.items():
        if all((symptom and symptom_value) or (not symptom and not symptom_value) for symptom_value, symptom in zip(disease_symptoms, symptoms)):
            possible_diseases.append(disease)
    return possible_diseases


# Function to search for diagnosis results by name
def search_diagnosis(patient_data, name):
    for patient in patient_data:
        if patient["name"] == name:
            return patient["diagnosis"]
    return "Patient not found"
