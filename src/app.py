import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns


# --- 1. Load the pre-trained model and scaler ---
@st.cache_resource
def load_components():
    # Вказуємо правильний шлях до файлів у папці src
    loaded_model = joblib.load('src/rf_model.pkl')
    loaded_scaler = joblib.load('src/scaler.pkl')
    return loaded_model, loaded_scaler


model, scaler = load_components()

# --- 2. Build the Streamlit User Interface ---
st.title("📞 Telecom Churn Prediction App")
st.write("Enter the customer's details below to predict the probability of them leaving the service.")

# Create input fields for all 9 predictive features
col1, col2 = st.columns(2)

with col1:
    is_tv_subscriber = st.selectbox("TV Subscriber", [1, 0])
    is_movie_package_subscriber = st.selectbox("Movie Package Subscriber", [1, 0])
    subscription_age = st.number_input("Subscription Age (years)", min_value=0.0, value=2.0)
    bill_avg = st.number_input("Average Bill ($)", min_value=0.0, value=20.0)
    reamining_contract = st.number_input("Remaining Contract (years)", min_value=0.0, value=0.0)

with col2:
    service_failure_count = st.number_input("Service Failure Count", min_value=0, value=0)
    download_avg = st.number_input("Average Download (GB)", min_value=0.0, value=10.0)
    upload_avg = st.number_input("Average Upload (GB)", min_value=0.0, value=2.0)
    download_over_limit = st.selectbox("Download Over Limit", [1, 0])

# --- 3. Process data and make prediction on button click ---
if st.button("Predict Churn Probability"):

    # Define feature names exactly as they were during model training
    feature_names = [
        'is_tv_subscriber', 'is_movie_package_subscriber', 'subscription_age',
        'bill_avg', 'reamining_contract', 'service_failure_count',
        'download_avg', 'upload_avg', 'download_over_limit'
    ]

    # Collect inputs into a list
    new_customer_data = [
        is_tv_subscriber, is_movie_package_subscriber, subscription_age,
        bill_avg, reamining_contract, service_failure_count,
        download_avg, upload_avg, download_over_limit
    ]

    # Convert to DataFrame
    new_data_df = pd.DataFrame([new_customer_data], columns=feature_names)

    # Scale only the numerical columns using the pre-fitted scaler
    cols_to_scale = ['subscription_age', 'bill_avg', 'reamining_contract',
                     'service_failure_count', 'download_avg', 'upload_avg']
    new_data_df[cols_to_scale] = scaler.transform(new_data_df[cols_to_scale])

    # Extract the probability for class 1 (Churn)
    probability = model.predict_proba(new_data_df)[0][1]

    # --- 4. Display the results and Visualization ---
    st.markdown("---")
    st.write(f"### Churn Probability: **{probability * 100:.2f}%**")

    # Text output based on threshold
    if probability > 0.5:
        st.error("⚠️ Result: The client has a HIGH probability of churn.")
        bar_color = 'salmon'
    else:
        st.success("✅ Result: The client has a LOW probability of churn.")
        bar_color = 'lightgreen'

    # Data Visualization directly in Streamlit
    fig, ax = plt.subplots(figsize=(8, 2))
    sns.barplot(x=[probability * 100], y=['Probability'], color=bar_color, ax=ax)
    ax.set_xlim(0, 100)
    ax.set_title('Churn Probability Indicator')
    ax.set_xlabel('Probability (%)')

    # Render the plot in the web app
    st.pyplot(fig)