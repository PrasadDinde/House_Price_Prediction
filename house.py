import streamlit as st
import pandas as pd
import pickle
import os

model_path = '/workspaces/House_Price_Prediction/model.pkl'  
if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
else:
    raise FileNotFoundError(f"The model file was not found at: {model_path}")

# Function to make predictions
def make_prediction(features):
    prediction = model.predict(features)
    return prediction

# Streamlit App
st.title("House Price Prediction")

# Input features
st.subheader("Enter House Features")

MedInc = st.number_input("MedInc", min_value=1.0000, max_value=10.000,step=0.01,value=3.0)
HouseAge  = st.number_input("Number of HouseAge",min_value=1.000,step=0.01,value=3.0)
AveRooms = st.number_input("Number of AveRooms",min_value=1.000,step=0.01,value=3.0)
AveBedrms = st.number_input("Number of AveBedrms", min_value=1.0000, max_value=10.000,step=0.01,value=3.0)
Population = st.number_input("Number of Population",min_value=1.000,step=0.001,value=3.0)

AveOccup = st.number_input("Number of AveOccup",min_value=1.0000,step=0.001,value=3.0)
Latitude = st.number_input("Latitude",min_value=1.000,step=0.01,value=3.0)
Longitude = st.number_input("Longitude",step=0.01,value=3.0)

# Create a DataFrame from the inputs
input_data = pd.DataFrame({
'MedInc':[MedInc],'HouseAge':[HouseAge],
'AveRooms':[AveRooms],'AveBedrms':[AveBedrms],
'Population':[Population],'AveOccup':[AveOccup],
'Latitude':[Latitude],'Longitude':[Longitude]})

st.write("Input Data:")
st.write(input_data)

# Button to trigger prediction
if st.button("Predict"):
    try:
        prediction = make_prediction(input_data)
        st.write(f"Predicted House Price: ${prediction[0]:.2f}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
