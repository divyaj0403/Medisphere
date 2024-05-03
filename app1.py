import os
import pickle
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Sidebar for navigation
selected = st.sidebar.selectbox('Multiple Disease Prediction System',
                                 ['Diabetes Prediction',
                                  'Heart Disease Prediction',
                                  "Parkinson's Prediction"])

# Load saved models
import os
import pickle

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the diabetes model
diabetes_model_path = os.path.join(current_dir, 'saved_models', 'diabetes_model.sav')
diabetes_model = pickle.load(open(diabetes_model_path, 'rb'))

# Load the heart disease model
heart_disease_model_path = os.path.join(current_dir, 'saved_models', 'heart_disease_model.sav')
heart_disease_model = pickle.load(open(heart_disease_model_path, 'rb'))

# Load the Parkinson's model
parkinsons_model_path = os.path.join(current_dir, 'saved_models', 'parkinsons_model.sav')
parkinsons_model = pickle.load(open(parkinsons_model_path, 'rb'))

# Function to predict diabetes
def predict_diabetes():
    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Function to predict heart disease
def predict_heart_disease():
    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Function to predict Parkinson's disease
def predict_parkinsons():
    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

# Main page content based on user selection
if selected == 'Diabetes Prediction':
    predict_diabetes()
elif selected == 'Heart Disease Prediction':
    predict_heart_disease()
elif selected == "Parkinson's Prediction":
    predict_parkinsons()
