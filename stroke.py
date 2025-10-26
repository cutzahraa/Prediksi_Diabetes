import streamlit as st
import pickle
import pandas as pd

# Fungsi utama aplikasi
def main():
    # Konfigurasi halaman
    st.set_page_config(page_title='Stroke Prediction App')

    # Sidebar
    st.sidebar.title('Stroke Prediction App')
    
    # Input fitur dari user
    gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
    gender = 1 if gender == "Male" else 0

    age = st.sidebar.number_input('Age', min_value=1, max_value=100, step=1)

    hypertension = st.sidebar.selectbox('Hypertension', ['No', 'Yes'])
    hypertension = 1 if hypertension == "Yes" else 0

    heart_disease = st.sidebar.selectbox('Heart Disease', ['No', 'Yes'])
    heart_disease = 1 if heart_disease == "Yes" else 0

    ever_married = st.sidebar.selectbox('Ever Married', ['No', 'Yes'])
    ever_married = 1 if ever_married == "Yes" else 0

    avg_glucose_level = st.sidebar.number_input('Average Glucose Level', min_value=1.0, max_value=300.0, step=1.0)
    bmi = st.sidebar.number_input('BMI', min_value=10.0, max_value=60.0, step=1.0)

    smoking_status = st.sidebar.selectbox('Smoking Status', ['Unknown', 'Never Smoked', 'Formerly Smoked', 'Smokes'])
    if smoking_status == "Unknown":
        smoking_status = 4
    elif smoking_status == "Never Smoked":
        smoking_status = 2
    elif smoking_status == "Formerly Smoked":
        smoking_status = 1
    elif smoking_status == "Smokes":
        smoking_status = 3

    # Buat dataframe dari input
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
    
    input_df = pd.DataFrame(input_data)

    # Load model
    model = pickle.load(open('stroke.pkl', 'rb'))

    # Tampilan utama
    st.title('PREDIKSI PENYAKIT STROKE')
    st.write('Selamat datang di aplikasi prediksi risiko stroke.')

    if st.button('Predict'):
        prediction = model.predict(input_df)[0]
        st.subheader("Hasil Prediksi:")
        if prediction == 0:
            st.success('✅ Tidak Ada Risiko Terjangkit Stroke')
        else:
            st.error('⚠️ Terdapat Risiko Terjangkit Stroke')


# Pastikan main() dijalankan
if __name__ == '__main__':
    main()
