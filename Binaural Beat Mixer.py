import numpy as np
from scipy.io.wavfile import write, read
from moviepy.editor import AudioFileClip, VideoFileClip

# Generate binaural beat (same as before)
sample_rate = 44100
duration = 5  # Adjust to match the length of your background music
frequency_left = 440
frequency_right = 445
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
tone_left = np.sin(2 * np.pi * frequency_left * t)
tone_right = np.sin(2 * np.pi * frequency_right * t)
binaural_beat = np.vstack((tone_left, tone_right)).T
binaural_beat = np.int16(binaural_beat * 32767)

# Save the binaural beat temporarily
write("temp_binaural_beat.wav", sample_rate, binaural_beat)

# Load the background music from an MP4 file
background_music = VideoFileClip("background_music.mp4").audio

# Extract the audio to a WAV file
background_music.write_audiofile("temp_background.wav")

# Load the background music WAV for manipulation
sample_rate, background = read("temp_background.wav")

# Ensure the binaural beat matches the background music length
if len(background) > len(binaural_beat):
    # Repeat the binaural beat to match the length
    repeats = len(background) // len(binaural_beat) + 1
    binaural_beat = np.tile(binaural_beat, (repeats, 1))[:len(background)]
else:
    binaural_beat = binaural_beat[:len(background)]

# Mix the binaural beat with the background music
# Adjust the volume of the binaural beat if necessary
mixed = background * 0.8 + binaural_beat * 0.2

# Ensure no clipping occurs
mixed = np.clip(mixed, -32767, 32767)

# Save the mixed audio back to a temporary WAV file
write("temp_mixed.wav", sample_rate, mixed.astype(np.int16))

# Combine the mixed audio with the original video (without audio)
final_clip = VideoFileClip("background_music.mp4").set_audio(AudioFileClip("temp_mixed.wav"))

# Save the final video with the binaural beat added to the background music
final_clip.write_videofile("final_output.mp4")
