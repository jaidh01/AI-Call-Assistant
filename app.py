import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase
import speech_recognition as sr
import tempfile

st.title("Streamlit Voice Assistant")

class AudioProcessor(AudioProcessorBase):
    def recv(self, frame):
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            f.write(frame.to_ndarray().tobytes())
            audio_path = f.name
        
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio)
                st.session_state['last_text'] = text
            except sr.UnknownValueError:
                st.session_state['last_text'] = "Could not understand audio"
            except sr.RequestError as e:
                st.session_state['last_text'] = f"Could not request results from Google Speech Recognition service; {e}"
        return frame

webrtc_streamer(key="mic", audio_processor_factory=AudioProcessor)

if 'last_text' in st.session_state:
    st.markdown(f"**You said:** {st.session_state['last_text']}")