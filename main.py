import streamlit as st

st.title("Weather Forecast for Next 5 Days")
place = st.text_input("Location: ")
day = st.slider("Forecast Days:", min_value=1, max_value=5, help="Select the number of forecasted day")
option = st.selectbox("Selext data to view",
                      ("Temperature", "Weather"))
st.subheader(f"{option} for the next {day} in {place}")
