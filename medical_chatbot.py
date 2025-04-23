import random

# Example rule-based responses
def medical_chatbot(input_symptom):
    symptoms_data = {
        "Fever": "You may have a viral infection. Drink plenty of fluids and rest.",
        "Cough": "You may have a cold or flu. Try drinking warm liquids and avoid cold environments.",
        "Headache": "Could be due to stress or dehydration. Rest and stay hydrated.",
        "Stomach Pain": "It might be indigestion. Avoid heavy meals for the next few hours."
    }
    
    response = symptoms_data.get(input_symptom, "I am not sure about this symptom. Please consult a doctor.")
    return response

# Example: Getting a response
input_symptom = "Cough"
response = medical_chatbot(input_symptom)
print(response)
