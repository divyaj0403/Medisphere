from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the hospital recommendation dataset CSV
doctor_data = pd.read_csv('doctor/doctor_data.csv')

def recommend_hospital(patient_location, patient_specialty):
    try:
        # Filter doctors by the patient's location and specialty
        hospitals_with_criteria = doctor_data[(doctor_data['Location'].str.contains(patient_location, case=False)) &
                                              (doctor_data['Specialties'].str.contains(patient_specialty, case=False))]

        if hospitals_with_criteria.empty:
            return {"error": "Sorry, there are no doctors in {} specializing in {}.".format(patient_location, patient_specialty)}

        # Sort hospitals by quality measures or any other relevant criteria
        recommended_hospital = hospitals_with_criteria.iloc[0]  # For simplicity, just recommend the first hospital

        return {"Doctor": recommended_hospital['Doctor Name'], "Location": recommended_hospital['Location']}
    except Exception as e:
        return {"error": "An error occurred: {}".format(e)}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendation', methods=['GET'])
def get_recommendation():
    location = request.args.get('location')
    specialty = request.args.get('specialty')
    return jsonify(recommend_hospital(location, specialty))

if __name__ == "__main__":
    app.run(debug=True)
