import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Path to your audio file
audio_file = "sample.wav"
# Load the audio file
with sr.AudioFile(audio_file) as source:
    print("Listening to audio...")
    audio_data = recognizer.record(source)

# Try converting speech to text
try:
    text = recognizer.recognize_google(audio_data)
    print("Transcription:")
    print(text)

except sr.UnknownValueError:
    print("Sorry, speech not recognized.")
except sr.RequestError as e:
    print(f"API error: {e}")
