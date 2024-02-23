import sounddevice as sd
import soundfile as sf

# Set the audio parameters
duration = 10  # Duration of the recording in seconds
filename = "recorded_audio.wav"  # Output audio file name
sample_rate = 44100  # Standard audio sample rate (44.1 kHz)

# Record audio
print(f"Recording {duration} seconds of audio...")
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
sd.wait()

# Save the recorded audio to a file
sf.write(filename, audio_data, sample_rate)

print(f"Audio saved to {filename}")
