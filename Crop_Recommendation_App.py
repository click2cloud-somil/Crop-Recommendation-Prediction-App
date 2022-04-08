# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 14:32:46 2022

@author: somil.mehta
"""

import pandas as pd
import pickle
import numpy as np
from PIL import Image
import streamlit as st


pickle_in = open("crop1.pkl","rb")
crop1 = pickle.load(pickle_in)  


def welcome():
    return "Welcome All"


def crop_recommendation(Temperature,Humidity,Rainfall,Nitrogen,Phosphorus,Potassium,pH):
    
    prediction = crop1.predict([[Temperature,Humidity,Rainfall,Nitrogen,Phosphorus,Potassium,pH]])
    print(prediction)
    return prediction


def main():
    #st.title("Crop Recommendation")
    html_temp = """
    <div style = "background-color:tomato;padding:10px">
    <h2 style = "color:white;text-align:center;">Crop Recommendation Web App </h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html = True)
    Temperature = st.text_input("Enter Temperature in °C")
    Humidity = st.text_input("Enter Humidity in %")
    Rainfall = st.text_input("Enter Rainfall in CM")
    Nitrogen = st.slider("Select Nitrogen quantity in KG/ha",min_value=0.0,max_value=150.0)
    Phosphorus = st.slider("Select Phosphorus quantity in KG/ha",min_value=0.0,max_value=100.0)
    Potassium = st.slider("Select Potassium quantity in KG/ha", min_value = 0.0,max_value = 90.0)
    pH = st.slider("Select pH range",min_value=4.530000,max_value=8.350000)
    
    
    result = ""
    if st.button("Predict"):
        result = crop_recommendation(Temperature,Humidity,Rainfall,Nitrogen,Phosphorus,Potassium,pH) 
    st.success("Recommended Crop : {}".format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")
        
if __name__=='__main__':
    main()        
    