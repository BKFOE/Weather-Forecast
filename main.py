import streamlit as st
import plotly.express as px

st.title("Weather Forecast for Next 5 Days")
place = st.text_input("Location: ")
day = st.slider("Forecast Days:", min_value=1, max_value=5, help="Select the number of forecasted day")
option = st.selectbox("Selext data to view",
                      ("Temperature", "Weather"))
st.subheader(f"{option} for the next {day} in {place}")


def get_data(day):
    dates = ["2023-09-06", "2023-09-07", "2023-09-08"]
    temperatures = [24, 25, 26]
    temperatures = [day * i for i in temperatures]
    return dates, temperatures


d, t = get_data(day)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
