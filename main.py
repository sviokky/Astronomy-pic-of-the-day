import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&thumbs=true"

response = requests.get(url)
data = response.json()


media_type = data.get("media_type")
title = data.get("title", "No title available")
explanation = data.get("explanation", "No description available")
media_url = data.get("url")


st.set_page_config(
    page_title="APOD",
    page_icon="⭐",
    layout="centered"
)

st.title("Astronomy Picture of the Day")
st.write("NASA's daily space content.")

st.subheader(title)

if media_type == "image":
    st.image(media_url)
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
            filter: blur(25px);
            transform: scale(1.1);
            z-index: -1;
        }}
        </style>
    
        <div class="bg"></div>
        """,
        unsafe_allow_html=True
    )
else:
    st.video(media_url)



st.write(explanation)
