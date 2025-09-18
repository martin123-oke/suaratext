import streamlit as st
import speech_recognition as sr

st.title("🎤 Ubah Suara ke Teks (Streamlit Cloud)")

# Ambil audio dari microphone
audio_file = st.audio_input("Rekam suara kamu:")

if audio_file is not None:
    st.audio(audio_file)

    # Simpan sementara file audio
    with open("temp.wav", "wb") as f:
        f.write(audio_file.getbuffer())

    # Gunakan SpeechRecognition
    recognizer = sr.Recognizer()
    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data, language="id-ID")
            st.success(f"Teks hasil suara: {text}")
        except sr.UnknownValueError:
            st.error("❌ Tidak bisa mengenali suara.")
        except sr.RequestError as e:
            st.error(f"⚠️ Gagal koneksi ke Google API: {e}")
