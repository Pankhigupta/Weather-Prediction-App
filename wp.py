import streamlit as st
import pickle as pkl

st.title("Weather Prediction App")
pn=st.number_input("Enter Precipitation")
maxt=st.number_input("Enter Maximum temperature")
mint=st.number_input("Enter Minimum temperature")
wind=st.number_input("Enter Wind speed")

button=st.button("Predict")
if button:
    lr=pkl.load(open("wp.pkl","rb"))
    res=lr.predict([[pn,maxt,mint,wind]])[0]
    st.markdown(f"today weather situation :{res}")
    
