import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import speech_recognition as sr

st.title("Speech to Text Online dengan Streamlit")

def callback(frame):
    audio = frame.to_ndarray()
    # audio processing bisa ditambahkan di sini
    return frame

webrtc_streamer(key="example", audio_receiver_size=256)
