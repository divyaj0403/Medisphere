import pandas as pd

# Load the hospital recommendation dataset CSV
doctor_data = pd.read_csv('doctor_data.csv')

def recommend_hospital(patient_location, patient_specialty):
    try:
        # Filter hospitals by the patient's location and specialty
        hospitals_with_criteria = doctor_data[(doctor_data['Location'].str.contains(patient_location, case=False)) & 
                                              (doctor_data['Specialties'].str.contains(patient_specialty, case=False))]

        if hospitals_with_criteria.empty:
            return "Sorry, there are no hospitals in {} specializing in {}.".format(patient_location, patient_specialty)
        # Sort hospitals by quality measures or any other relevant criteria
        recommended_hospital = hospitals_with_criteria.iloc[0]  # For simplicity, just recommend the first hospital

        return recommended_hospital['Doctor Name'], recommended_hospital['Location'], recommended_hospital['Experience']
    except Exception as e:
        return "An error occurred: {}".format(e)

def main():
    print("Welcome to the: Know the Doctor in your Area:")
    patient_location = input("Please enter your Location: ").strip().capitalize()
    patient_specialty = input("Please enter the specialist: ").strip().capitalize()

    recommended_doctor, location = recommend_hospital(patient_location, patient_specialty)

    print("\nRecommended Doctor for {} in {}: {} ({})".format(patient_specialty, patient_location, recommended_doctor, location))

if __name__ == "__main__":
    main()
