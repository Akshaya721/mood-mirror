import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from tone_data import get_emotion_and_reply
import requests
import time
import json
import random

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
        background: -webkit-linear-gradient(90deg, hsla(340, 80%, 69%,