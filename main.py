import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)
data = response.json()

image_url = data.get("url")
media_type = data.get("media_type")

st.set_page_config(
    page_title="APOD",
    page_icon="⭐",
    layout="centered"
)
if media_type == "image" and image_url:
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: transparent;
        }}
    
        .bg {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url("{data["url"]}");
            background-size: cover;
            background-position: center;
            filter: blur(15px);
            transform: scale(1.1);
            z-index: -1;
        }}
        </style>
    
        <div class="bg"></div>
        """,
        unsafe_allow_html=True
    )

else:
    st.warning("Today's APOD is not an image (it may be a video).")

st.title("Astronomy Picture of the Day")
st.write("This webpage shows the picture of the day by NASA every day")

st.subheader(data.get("title", "No title available"))

if media_type == "image":
    st.image(image_url)
else:
    st.video(image_url)

st.write(data.get("explanation", "No description available"))