from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Possible symptoms, diseases, medicines, and workouts
symptoms = ["Fever", "Cough", "Headache", "Stomach Pain", "Chest Pain", "Rash", "Weakness", "Shortness of Breath",
            "Joint Pain", "Nausea", "Runny Nose", "Sore Throat", "Dizziness", "Blurred Vision", "Back Pain",
            "Fatigue", "Insomnia", "Vomiting", "Constipation", "Diarrhea", "High Blood Pressure", "Low Blood Sugar",
            "Ear Pain", "Eye Irritation", "Skin Itching", "Knee Pain", "Memory Loss", "Swelling", "Frequent Urination",
            "Numbness", "Muscle Cramps", "Cold Hands", "Weight Loss", "Weight Gain", "Anxiety", "Depression",
            "Hair Loss", "Dry Skin", "Night Sweats", "Heart Palpitations", "Tingling Sensation", "Nosebleeds",
            "Brittle Nails", "Vision Problems", "Swollen Lymph Nodes", "Slow Healing Wounds", "Increased Thirst",
            "Dark Urine", "Lightheadedness"]

diseases = ["Flu", "Cold", "Migraine", "Indigestion", "Heart Problem", "Allergy", "Anemia", "Asthma", "Arthritis",
            "Food Poisoning", "Sinusitis", "Tonsillitis", "Low Blood Pressure", "Diabetes", "Muscle Strain",
            "Chronic Fatigue Syndrome", "Stress", "Gastroenteritis", "Hypertension", "Hypoglycemia", "Otitis",
            "Conjunctivitis", "Eczema", "Osteoarthritis", "Alzheimer’s", "Kidney Disease", "Urinary Infection",
            "Nerve Damage", "Thyroid Disorder", "Vitamin Deficiency", "Hormonal Imbalance", "Pneumonia", "Bronchitis"]

medicines = ["Paracetamol", "Ibuprofen", "Antacids", "ORS solution", "Salbutamol inhaler", "Hydrocortisone cream",
             "Iron supplements", "Calcium supplements", "Activated charcoal", "Antibiotics", "Salt tablets",
             "Glucose tablets", "Beta-blockers", "Melatonin", "Cholinesterase inhibitors", "Diuretics",
             "Vitamin B12 supplements", "Decongestants", "Laxatives", "Corticosteroid creams", "Angiotensin inhibitors"]

workouts = ["Rest for 2-3 days", "Steam inhalation", "Light stretching", "Physiotherapy", "Regular exercise",
            "Yoga & meditation", "Breathing exercises", "Light walking", "Cardio exercises", "Strength training",
            "Muscle relaxation", "Eye exercises", "Aerobic workouts", "Massage therapy", "Dietary adjustments"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['user_input']

    # You can integrate a more advanced model or rule-based logic here
    response = "Based on your symptom: '{}' we suggest the following: \n\n".format(user_input)
    response += random.choice(diseases) + "\n"
    response += "Medicine: " + random.choice(medicines) + "\n"
    response += "Recommended workout: " + random.choice(workouts)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
