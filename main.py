from functions import symptoms, search_diagnosis, make_diagnosis

# List of dictionaries to store diagnoses
patient_compendium = []

# Request diagnostic information for a person
def get_patient_diagnosis():
    patient_name = input("Enter the person's name: ")
    person_symptoms = []
    for symptom in symptoms:
        answer = input(f"Do you have {symptom}? (Y/N): ").lower()
        person_symptoms.append(answer == "y")
    
    person_diagnosis = make_diagnosis(person_symptoms)
    return {"name": patient_name, "symptoms": person_symptoms, "diagnosis": person_diagnosis}

# Main loop
while True:
    option = input("What would you like to do? (1-Add/2-Search/3-Exit): ").lower()
    
    if option == "1":
        patient_data = get_patient_diagnosis()
        patient_compendium.append(patient_data)
        print("Diagnosis successfully added.")
        
        # Show suggested diagnoses for the patient
        print("Suggested diagnoses:")
        for diagnosis in patient_data["diagnosis"]:
            print("- " + diagnosis)
        
    elif option == "2":
        patient_name = input("Enter the person's name to search for the diagnosis: ")
        result = search_diagnosis(patient_compendium, patient_name)
        
        if isinstance(result, list):
            print(f"Possible diagnoses for {patient_name}:")
            for diagnosis in result:
                print("- " + diagnosis)
        else:
            print(f"{patient_name}'s diagnosis: {result}")
        
    elif option == "3":
        print("Goodbye!")
        break
    
    else:
        print("Invalid option. Please choose between 1-Add, 2-Search, or 3-Exit.")
