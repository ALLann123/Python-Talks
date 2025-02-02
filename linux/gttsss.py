from gtts import gTTS
import pygame
import io

# Create the TTS object
tts = gTTS('hello, I am shadow. How can I help you sir.')

# Create a bytes buffer to hold the audio data
mp3_data = io.BytesIO()
tts.write_to_fp(mp3_data)
mp3_data.seek(0)

# Initialize pygame mixer
pygame.mixer.init()

# Load and play the speech from the buffer
pygame.mixer.music.load(mp3_data, 'mp3')
pygame.mixer.music.play()

# Wait for the speech to finish
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
