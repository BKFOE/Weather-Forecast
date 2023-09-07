import streamlit as st
import plotly.express as px
import backend as be

# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for Next 5 Days")
place = st.text_input("Location: ")
day = st.slider("Forecast Days:", min_value=1, max_value=5, help="Select the number of forecasted day")
option = st.selectbox("Selext data to view",
                      ("Temperature", "Weather"))
st.subheader(f"{option} for the next {day} in {place}")

if place:
    # Get the temperature/ weather data
    filtered_data = be.get_data(place, day)

    # Create a temperature plot
    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Weather":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        weather_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_path = [images[condition] for condition in weather_conditions]
        st.image(image_path, width=115)
