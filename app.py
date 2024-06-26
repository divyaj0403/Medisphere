from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the hospital recommendation dataset CSV
hospital_data = pd.read_csv('hospital_recommendation_dataset_UPDATED.csv')

def recommend_hospital(patient_illness):
    # Filter hospitals by the patient's illness
    hospitals_with_illness = hospital_data[hospital_data['Specialties'].str.contains(patient_illness, case=False)]

    if hospitals_with_illness.empty:
        return {"error": "Sorry, there are no hospitals specializing in {}.".format(patient_illness)}

    # Sort hospitals by quality measures or any other relevant criteria
    recommended_hospital = hospitals_with_illness.iloc[0]  # For simplicity, just recommend the first hospital

    return {"hospital": recommended_hospital['Hospital Name'], "location": recommended_hospital['Location']}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendation', methods=['GET'])
def get_recommendation():
    illness = request.args.get('illness')
    return jsonify(recommend_hospital(illness))

if __name__ == "__main__":
    app.run(debug=True)
