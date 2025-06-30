import json
import random
import requests
import streamlit as st
import time
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
import gspread

try:
    from tone_data import get_emotion_and_reply, emotions
except ImportError:
    emotions = None  # Fallback if tone_data.py or emotions is missing

# Streamlit page config
st.set_page_config(page_title="Mood Mirror", layout="centered")

# Initial CSS
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
creds_json = st.secrets["google_credentials"]["content"]
creds_dict = json.loads(creds_json)
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)
sheet = client.open("Mood Mirror Logs").sheet1

# Mood-specific emojis and backgrounds
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
    "tired": "https://images.pexels.com/photos/32740698/pexels-photo-32740698/free-photo-of-aerial-view-of-a-serene-beach-with-a-lone-walker.jpeg",
    "sad": "https://images.pexels.com/photos/6128370/pexels-photo-6128370.jpeg",
    "angry": "https://images.pexels.com/photos/1054218/pexels-photo-1054218.jpeg",
    "anxious": "https://images.pexels.com/photos/1323550/pexels-photo-1323550.jpeg",
    "happy": "https://images.unsplash.com/photo-1543862475-eb136770ae9b",
    "frustrated": "https://images.pexels.com/photos/210243/pexels-photo-210243.jpeg",
    "helpless": "https://images.unsplash.com/photo-1510673398445-94f476ef2cbc",
    "bored": "https://plus.unsplash.com/premium_photo-1680686089517-862755ff8616",
    "grumpy": "https://images.pexels.com/photos/268134/pexels-photo-268134.jpeg",
    "nervous": "https://images.pexels.com/photos/32550942/pexels-photo-32550942/free-photo-of-lush-terraced-hills-in-dagestan-russia.jpeg",
    "relaxed": "https://images.pexels.com/photos/189349/pexels-photo-189349.jpeg",
    "insecure": "https://images.pexels.com/photos/8709627/pexels-photo-8709627.jpeg",
    "overwhelmed": "https://images.unsplash.com/photo-1553078954-b5770add7a4e",
    "grateful": "https://images.pexels.com/photos/673018/pexels-photo-673018.jpeg",
    "hopeful": "https://images.unsplash.com/photo-1495559493698-ae68846c94e8",
    "motivated": "https://images.unsplash.com/photo-1656716870961-9cc8345ac4e3",
    "lonely": "https://images.pexels.com/photos/32756394/pexels-photo-32756394/free-photo-of-lonely-figure-walking-through-flower-field.png",
    "unknown": "https://images.pexels.com/photos/1266810/pexels-photo-1266810.jpeg"
}

# Hugging Face API setup
HF_API_URL = "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"
try:
    HF_API_TOKEN = st.secrets["HF_API_TOKEN"]
except KeyError:
    st.warning("Hugging Face API token not found. Using fallback emotion detection. Please configure HF_API_TOKEN in secrets.toml.")
    HF_API_TOKEN = None

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
            emotion = "unknown"
            reply = random.choice(local_emotions["unknown"]["replies"])  # Default fallback
            try:
                if HF_API_TOKEN:
                    # Try Hugging Face API
                    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
                    payload = {"inputs": user_input}
                    response = requests.post(HF_API_URL, headers=headers, json=payload)
                    response.raise_for_status()
                    results = response.json()[0]  # List of emotion scores
                    # Find the emotion with the highest score
                    primary_emotion = max(results, key=lambda x: x['score'])['label']
                    # Map Hugging Face emotions to your emotions
                    emotion_map = {
                        "joy": "happy",
                        "sadness": "sad",
                        "anger": "angry",
                        "fear": "anxious",
                        "surprise": "hopeful",
                        "disgust": "frustrated",
                        "neutral": "neutral"
                    }
                    emotion = emotion_map.get(primary_emotion, "unknown")
                    # Use local_emotions as the base, override with tone_data.py if available
                    reply = random.choice(local_emotions[emotion]["replies"])
                    if emotions and emotion in emotions:
                        reply = random.choice(emotions[emotion]["replies"])
                else:
                    raise ValueError("No valid Hugging Face API token provided.")
            except (requests.RequestException, KeyError, IndexError, ValueError) as e:
                st.warning(f"Hugging Face API failed: {str(e)}. Using fallback emotion detection.")
                # Fallback to tone_data.py
                try:
                    emotion, reply = get_emotion_and_reply(user_input)
                except Exception as e:
                    st.warning(f"Fallback detection failed: {str(e)}. Using default reply.")
                    emotion = "unknown"
                    reply = random.choice(local_emotions["unknown"]["replies"])

            # Log to Google Sheets
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sheet.append_row([timestamp, user_input, emotion, reply])

            # Update background and display response
            emoji = mood_emojis.get(emotion.lower(), "😐")
            background_path = mood_backgrounds.get(emotion.lower(), mood_backgrounds["unknown"])
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