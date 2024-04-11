import numpy as np
from scipy.io.wavfile import write

# Settings
sample_rate = 44100  # CD-quality audio
duration = 5  # in seconds
frequency_left = 440  # A4 note, for example
frequency_right = 445  # A slightly higher frequency for the binaural effect

# Generate time points
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generate sine wave tones
tone_left = np.sin(2 * np.pi * frequency_left * t)
tone_right = np.sin(2 * np.pi * frequency_right * t)

# Combine into a stereo signal
stereo_tone = np.vstack((tone_left, tone_right)).T

# Convert to 16-bit data
stereo_tone = np.int16(stereo_tone * 32767)

# Write to a WAV file
write("binaural_beat.wav", sample_rate, stereo_tone)
