import pandas as pd
# Load the hospital recommendation dataset CSV
hospital_data = pd.read_csv('hospital_recommendation_dataset_UPDATED.csv')

def recommend_hospital(patient_illness):
    # Filter hospitals by the patient's illness
    hospitals_with_illness = hospital_data[hospital_data['Specialties'].str.contains(patient_illness, case=False)]

    if hospitals_with_illness.empty:
        return "Sorry, there are no hospitals specializing in {}.".format(patient_illness)
    # Sort hospitals by quality measures or any other relevant criteria
    recommended_hospital = hospitals_with_illness.iloc[0]  # For simplicity, just recommend the first hospital

    return recommended_hospital['Hospital Name'], recommended_hospital['Location']

def main():
    print("Welcome to the Hospital Recommendation System!")
    patient_illness = input("Please enter your illness: ").strip().capitalize()

    recommended_hospital, location = recommend_hospital(patient_illness)

    print("\nRecommended Hospital for {}: {} ({})".format(patient_illness, recommended_hospital, location))

if __name__ == "__main__":
    main()
