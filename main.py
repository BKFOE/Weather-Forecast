import streamlit as st
import plotly.express as px
import backend as be

st.title("Weather Forecast for Next 5 Days")
place = st.text_input("Location: ")
day = st.slider("Forecast Days:", min_value=1, max_value=5, help="Select the number of forecasted day")
option = st.selectbox("Selext data to view",
                      ("Temperature", "Weather"))
st.subheader(f"{option} for the next {day} in {place}")


d, t = be.get_data(place, day, option)


figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
