import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use the default microphone as the audio source
microphone = sr.Microphone()

# Adjust for ambient noise
with microphone as source:
    recognizer.adjust_for_ambient_noise(source)



# Capture live speech and convert to text
try:
    while True:
        print("Listening...")
        with microphone as source:
            audio = recognizer.listen(source)

        # Perform speech recognition
        text = recognizer.recognize_google(audio)
        print("You said:", text)

except KeyboardInterrupt:
    print("Stopped listening.")
