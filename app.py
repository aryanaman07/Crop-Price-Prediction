import streamlit as st
import pandas as pd
import warnings

import pickle

# Ignore warnings
warnings.filterwarnings('ignore')

# CSS to add background image
background_image_css = """
<style>
    .stApp {
        background-image: url('https://static.vecteezy.com/system/resources/previews/027/004/037/non_2x/green-natural-leaves-background-free-photo.jpg');  /* Replace with your image URL */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
</style>
"""
st.markdown(background_image_css, unsafe_allow_html=True)

# Streamlit app title and description
st.title("AGRI-FORECAST")
st.header("Predict Future Values of Agri-Horticulture Commodities")
st.subheader("Enter the Zone, Season, Commodity, Month, and Year for which you need predictions, and get the predicted average sales for that month.")

# Zone selection box
zone = st.selectbox("ZONE", ["North", "South", "East", "West", "Central", "Northeast"])

# Season selection box
season = st.selectbox("SEASON", ["Winter", "Spring", "Summer", "Monsoon", "Autumn", "Pre-Winter"])

# Commodity selection box
com = st.selectbox("COMMODITY", 
                   ["Gram Dal", "Sugar", "Gur", "Wheat", "Tea", "Milk", "Salt", "Atta", 
                    "Tur/Arhar Dal", "Urad Dal", "Moong Dal", "Masoor Dal", 
                    "Groundnut Oil", "Mustard Oil", "Vanaspati", "Sunflower Oil", 
                    "Soya Oil", "Palm Oil", "Rice", "Potato", "Onion", "Tomato"])

# Load pickle files for each commodity
with open("combined_series_Dal.pkl", "rb") as f:
    dal = pickle.load(f)
with open("combined_series_Gur.pkl", "rb") as f:
    gur = pickle.load(f)
with open("combined_series_Milk.pkl", "rb") as f:
    milk = pickle.load(f)
with open("combined_series_Salt.pkl", "rb") as f:
    salt = pickle.load(f)
with open("combined_series_Sugar.pkl", "rb") as f:
    sugar = pickle.load(f)
with open("combined_series_Tea.pkl", "rb") as f:
    tea = pickle.load(f)
with open("combined_series_Wheat.pkl", "rb") as f:
    wheat = pickle.load(f)

st.subheader('Get Prediction or Historical Value for a Specific Month and Year')
year = st.number_input("Enter the Year", min_value=2014, max_value=2034, value=2024)
month = st.selectbox("Enter the Month", list(range(1, 13)), index=0)

if st.button("Get Value"):
    # Construct the date string for lookup
    date = f"{year}-{month:02d}-01"
    
    # Retrieve the value based on the selected commodity
    if com == "Gram Dal":
        value = dal.get(date, None)
    elif com == "Sugar":
        value = sugar.get(date, None)
    elif com == "Gur":
        value = gur.get(date, None)
    elif com == "Wheat":
        value = wheat.get(date, None)
    elif com == "Tea":
        value = tea.get(date, None)
    elif com == "Milk":
        value = milk.get(date, None)
    elif com == "Salt":
        value = salt.get(date, None)
    else:
        value = None
    
    # Display the result with two decimal places if value is numeric
    if value is not None:
        try:
            st.header(f"Price of {com} on {date}: {float(value):.2f}")
        except ValueError:
            st.header("Data format error. Unable to display value.")
    else:
        st.subheader("Data not available for the selected date.")
