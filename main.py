import streamlit as st
import requests

st.markdown(
    """
    <style>
    .stApp {
        background: transparent;
    }

    /* Background layer */
    .bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa");
        background-size: cover;
        background-position: center;
        filter: blur(12px);
        transform: scale(1.1);
        z-index: -1;
    }
    </style>

    <div class="bg"></div>
    """,
    unsafe_allow_html=True
)

api_key = "2QtJ2e56PrhcQB5fSZhZC7xebRMXH7zPIeu27PCy"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)
data = response.json()


st.set_page_config(
    page_title="APOD",
    page_icon="⭐",
    layout="centered"
)

st.title("Astronomy Picture of the Day")
st.write("This webpage shows the picture of the day by NASA every day")
st.write(data["title"])
st.image(data["url"])
st.write(data["explanation"])
