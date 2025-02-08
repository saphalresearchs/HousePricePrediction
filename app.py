import streamlit as st
import pickle
import numpy as np
# from xgboost import XGBRegressor

with open("model.pkl","rb") as file:
    pickle.load(file)

model = pickle.load(open("model.pkl", "rb"))


st.title("Boston House Price Predictinn")

st.write("Enter the required details to predict house prices: ")

#inputfields
CRIM = st.number_input("CRIM", min_value= 0.0, max_value= 100.0, step=0.002)	
ZN = st.number_input("ZN", min_value=0, max_value=100, step=1) 
INDUS = st.number_input("INDUS", min_value=0.0, max_value=100.0, step=0.5)	
CHAS = st.number_input("CHAS", min_value=0.0, max_value=1.0, step=0.01)	
NOX = st.number_input("NOX", min_value=0.0, max_value=1.0, step=0.01)	
RM = st.number_input("RM", min_value=0.0, max_value=9.0, step=0.01)	
AGE = st.number_input("AGE", min_value=0.0, max_value=150.0, step=0.1)	
DIS = st.number_input("DIS", min_value=0.0, max_value=50.0, step=0.01)	
RAD = st.number_input("RAD", min_value=1, max_value=24, step=1)	
TAX = st.number_input("TAX", min_value=0, max_value=10000, step=1)	
PTRATIO = st.number_input("PTRATIO", min_value=0.0, max_value=100.0, step=0.1)	
B = st.number_input("B", min_value=0, max_value=1000, step=1)	
LSTAT = st.number_input("LSTAT", min_value=0.0, max_value=100.0, step=0.1)

if st.button("Predict"):
    input_data = np.asarray([CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT])
    input_data_reshaped = input_data.reshape(1,-1)
    prediction = model.predict(input_data_reshaped)
    st.write("The price of house is: $", round(prediction[0]*1000,2))

