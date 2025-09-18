import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, AudioProcessorBase
import av
import speech_recognition as sr

st.title("🎤 Speech to Text Online dengan Streamlit")

class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recv_audio(self, frame: av.AudioFrame):
        audio = frame.to_ndarray()
        # Konversi ke objek AudioData
        audio_data = sr.AudioData(
            audio.tobytes(),
            frame.sample_rate,
            audio.dtype.itemsize * 8
        )
        try:
            text = self.recognizer.recognize_google(audio_data, language="id-ID")
            st.session_state["last_text"] = text
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            st.warning(f"Google API error: {e}")
        return frame

webrtc_streamer(
    key="speech-to-text",
    mode=WebRtcMode.SENDRECV,
    audio_processor_factory=AudioProcessor,
    media_stream_constraints={"audio": True, "video": False},
)

if "last_text" in st.session_state:
    st.subheader("Hasil Transkripsi 🎙️")
    st.write(st.session_state["last_text"])
