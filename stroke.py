import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier

# Create a function to preprocess the data
def main():
    
    # Set page title
    st.set_page_config(page_title='Stroke Prediction App')
    # st.set_page_config(page_footer='Asril Murdian Tahir')
    # Set heading
    st.sidebar.title('Stroke Prediction App')
    
    # Input fields for features
    gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
    if gender=="Male":
        gender=1
    else:
        gender=0
    age = st.sidebar.number_input('Age', min_value=1, max_value=100, step=1)
    hypertension = st.sidebar.selectbox('Hypertension', ['No', 'Yes'])
    if hypertension=="Yes":
        hypertension=1
    else:
        hypertension=0
    heart_disease = st.sidebar.selectbox('Heart Disease', ['No', 'Yes'])
    if heart_disease=="Yes":
        heart_disease=1
    else:
        heart_disease=0
    ever_married = st.sidebar.selectbox('Ever Married', ['No', 'Yes'])
    if ever_married=="Yes":
        ever_married=1
    else:
        ever_married=0
    avg_glucose_level = st.sidebar.number_input('Average Glucose Level', min_value=1.0, max_value=300.0, step=1.0)
    bmi = st.sidebar.number_input('BMI', min_value=10.0, max_value=60.0, step=1.0)
    smoking_status = st.sidebar.selectbox('Smoking Status', ['Unknown', 'Never Smoked', 'Formerly Smoked', 'Smokes'])
    if smoking_status=="Unknown":
        smoking_status=4
    elif smoking_status=="Never Smoked":
        smoking_status=2
    elif smoking_status=="Formerly Smoked":
        smoking_status=1
    elif smoking_status=="Smokes":
        smoking_status=3

    # Create a dictionary with input data
    input_data = {
        'gender': [gender],
        'age': [age],
        'hypertension': [hypertension],
        'heart_disease': [heart_disease],
        'ever_married': [ever_married],
        'avg_glucose_level': [avg_glucose_level],
        'bmi': [bmi],
        'smoking status': [smoking_status]
    }
    
    # Create a DataFrame from the input data
    input_df = pd.DataFrame(input_data)
    
    # Train the model
    model = pickle.load(open('stroke.pkl', 'rb'))
    
    # Make predictions
    
    st.title('PREDIKSI PENYAKIT STROKE')
    st.write('Selamat datang di website kami!')
    # Display the prediction
    st.title("Hasil Klasifikasinya Adalah")
    if st.button('Predict'):
        # Make predictions
        prediction = model.predict(input_df)[0]
        
        # Display the prediction
        if prediction == 0:
            st.write('Tidak Ada Resiko Terjangkit Stroke')
        else:
            st.write('Terdapat resiko terjangkit stroke')

    if __name__ == '__main__':
     main()    