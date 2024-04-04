import streamlit as st
import speech_recognition as sr

# Initializing the recognizer
r = sr.Recognizer()

def record_text():
    # Use microphone as a source of input
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        
        # Listens for the user input
        audio = r.listen(source)
        
        # Using Google to recognize audio
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            st.warning("Could not understand audio")
        except sr.RequestError as e:
            st.error(f"Could not request results: {e}")

def output_text(text):
    with open("speechtest.txt", "a") as f:
        f.write(text + "\n")

def main():
    st.title("Speech to Text Recorder")
    
    record_state = st.button("Record")
    stop_state = st.button("Stop")
    
    if record_state:
        st.info("Recording...")
        text = record_text()
        output_text(text)
        st.success("Recording complete")
    
    if stop_state:
        st.info("Recording stopped")

    st.subheader("Recorded Text")
    with open("speechtest.txt", "r") as f:
        recorded_text = f.read()
    st.text_area("Recorded Text", recorded_text, height=200)

if __name__ == "__main__":
    main()
