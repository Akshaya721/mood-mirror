import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from tone_data import get_emotion_and_reply
import time

st.set_page_config(page_title="Mood Mirror", layout="centered")

# Initial CSS with gradient background
st.markdown("""
    <style>
    .stApp {
        height: 100%;
        background: hsla(340, 80%, 69%, 1);
        background: linear-gradient(90deg, hsla(340, 80%, 69%, 1) 0%, hsla(15, 93%, 71%, 1) 100%);
        background: -moz-linear-gradient(90deg, hsla(340, 80%, 69%, 1) 0%, hsla(15, 93%, 71%, 1) 100%);
        background: -webkit-linear-gradient(90deg, hsla(340, 80%, 69%, 1) 0%, hsla(15, 93%, 71%, 1) 100%);
        filter: progid: DXImageTransform.Microsoft.gradient(startColorstr="#EF709B", endColorstr="#FA9372", GradientType=1);
        font-family: 'Segoe UI', sans-serif;
        transition: background 0.5s ease;
    }
    .stTextArea textarea {
        font-size: 16px !important;
        height: 80px !important;
        padding: 0.75rem;
        border-radius: 12px;
        transition: transform 0.3s ease;
    }
    .stTextArea textarea:focus {
        animation: bounce 0.5s ease;
    }
    @keyframes bounce {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .response-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
        margin-top: 20px;
        font-size: 18px;
        animation: slideIn 0.8s ease-in-out;
    }
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    </style>
""", unsafe_allow_html=True)

# Google Sheets Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Mood Mirror Logs").sheet1

# Mood-specific emojis and background images
mood_emojis = {
    "tired": "😴",
    "sad": "😢",
    "angry": "😣",
    "anxious": "😓",
    "happy": "😄",
    "frustrated": "😣",
    "helpless": "😞",
    "bored": "😑",
    "grumpy": "😕",
    "nervous": "😬",
    "relaxed": "😊",
    "insecure": "😔",
    "overwhelmed": "😰",
    "grateful": "🙏",
    "hopeful": "🌱",
    "motivated": "💪",
    "lonely": "😶",
    "neutral": "😐",
    "unknown": "🤔"
}
mood_backgrounds = {
    "tired": "https://images.pexels.com/photos/936722/pexels-photo-936722.jpeg",  # Cozy bedroom
    "sad": "https://images.pexels.com/photos/167964/pexels-photo-167964.jpeg",  # Rainy day
    "angry": "https://images.pexels.com/photos/672532/pexels-photo-672532.jpeg",  # Dark forest
    "anxious": "https://images.pexels.com/photos/1391457/pexels-photo-1391457.jpeg",  # Stormy ocean
    "happy": "https://images.pexels.com/photos/531321/pexels-photo-531321.jpeg",  # Sunny field
    "frustrated": "https://images.pexels.com/photos/417323/pexels-photo-417323.jpeg",  # Mountain sunset
    "helpless": "https://images.pexels.com/photos/417074/pexels-photo-417074.jpeg",  # Foggy hills
    "bored": "https://images.pexels.com/photos/1040626/pexels-photo-1040626.jpeg",  # Empty room
    "grumpy": "https://images.pexels.com/photos/207962/pexels-photo-207962.jpeg",  # Cloudy sky
    "nervous": "https://images.pexels.com/photos/1450361/pexels-photo-1450361.jpeg",  # Dark alley
    "relaxed": "https://images.pexels.com/photos/1103970/pexels-photo-1103970.jpeg",  # Serene lake
    "insecure": "https://images.pexels.com/photos/1484567/pexels-photo-1484567.jpeg",  # Mirror reflection
    "overwhelmed": "https://images.pexels.com/photos/417173/pexels-photo-417173.jpeg",  # Busy city
    "grateful": "https://images.pexels.com/photos/1454809/pexels-photo-1454809.jpeg",  # Sunset gratitude
    "hopeful": "https://images.pexels.com/photos/110854/pexels-photo-110854.jpeg",  # Sunrise
    "motivated": "https://images.pexels.com/photos/416160/pexels-photo-416160.jpeg",  # Mountain climb
    "lonely": "https://images.pexels.com/photos/1037992/pexels-photo-1037992.jpeg",  # Empty bench
    "neutral": "https://images.pexels.com/photos/417074/pexels-photo-417074.jpeg",  # Balanced green hills
    "unknown": "https://images.pexels.com/photos/1287149/pexels-photo-1287149.jpeg"  # Abstract nature
}

# Title and subtitle
st.markdown("<h1 style='text-align: center;'>🌈 Mood Mirror</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic;'>Tell me how you're feeling, and I’ll reflect a kind thought.</p>", unsafe_allow_html=True)
st.markdown("### 📝 Write what you’re feeling in 1–2 lines...")

# Input Box
user_input = st.text_area(" ", placeholder="e.g., I’m feeling lowkey sad today.", max_chars=200, label_visibility="collapsed")

# Reflect Button
if st.button("✨ Reflect"):
    user_input = user_input.strip()
    if user_input:
        with st.spinner("Reflecting your mood..."):
            time.sleep(1.2)
            emotion, reply = get_emotion_and_reply(user_input)
            print(f"Input: '{user_input}'")  # Log the exact input
            print(f"Detected emotion: '{emotion}'")  # Log the detected emotion
            print(f"Available moods: {list(mood_backgrounds.keys())}")  # List all expected moods
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sheet.append_row([timestamp, user_input, emotion, reply])
        
        # Update background with mood-specific image
        emoji = mood_emojis.get(emotion.lower(), "😐")
        background_path = mood_backgrounds.get(emotion.lower(), mood_backgrounds["neutral"])
        st.markdown(f"""
            <style>
            .stApp {{
                background: url('{background_path}') no-repeat center center fixed;
                background-size: cover;
            }}
            </style>
        """, unsafe_allow_html=True)
        
        st.markdown(f"<div class='response-box'>{reply} {emoji}</div>", unsafe_allow_html=True)
    else:
        st.warning("Please type something to reflect on.")