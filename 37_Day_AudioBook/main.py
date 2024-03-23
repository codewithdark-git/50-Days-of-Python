from gtts import gTTS
import os

file_path = "Enter your file path"

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Initialize the gTTS engine
tts = gTTS(text, lang='en')

# Save the audio to an MP3 file
output_file = 'audiobook.mp3'
tts.save(output_file)
print(f"{output_file} has been save ")

# Play the audiobook
os.system(f"start {output_file}")
