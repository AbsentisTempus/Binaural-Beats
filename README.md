# Binaural Beats Generator and Mixer

This project consists of two Python scripts designed for audio manipulation, particularly focusing on binaural beats. The first script generates a binaural beat, and the second script adds this beat to a background music track extracted from an MP4 file, mixing them together into a final output that's saved as an MP4 file.

## Scripts

### Binaural Beat Generator

`binaural_beat_generator.py` is a script that generates a binaural beat audio file. Binaural beats are auditory illusions perceived when two different pure-tone sine waves, both with frequencies lower than 1500 Hz and with less than a 40 Hz difference between them, are presented to a listener dichotically (one through each ear).

#### Features

- Generates a stereo WAV file with a binaural beat.
- Customizable frequency for each ear to create different types of binaural beats (e.g., for relaxation, focus, etc.).

### Binaural Beat Mixer

`binaural_beat_mixer.py` takes the generated binaural beat and mixes it with the audio extracted from a provided MP4 file. This allows for the overlay of binaural beats onto existing music tracks or ambient sounds, creating a combined audio experience.

#### Features

- Extracts audio from an MP4 file.
- Mixes the extracted audio with a binaural beat.
- Saves the mixed audio with the original video content into a new MP4 file.

## Setup

To run these scripts, you need Python installed on your machine along with some additional libraries. Use the following command to install the required libraries:

```bash
pip install numpy scipy moviepy
```

## Usage

### Generating a Binaural Beat

Run `binaural_beat_generator.py` and specify the desired frequencies for the left and right ear tones. The script will generate a WAV file named `binaural_beat.wav`.

```bash
python binaural_beat_generator.py
```

### Mixing the Binaural Beat with Background Music

After generating the binaural beat, run `binaural_beat_mixer.py` with the path to your MP4 file containing the background music or ambient sound.

```bash
python binaural_beat_mixer.py --input background_music.mp4
```

The script will produce a final MP4 file named `final_output.mp4` that combines the video from `background_music.mp4` with the mixed audio track.

## Customization

You can customize the frequencies used in the binaural beat, the duration of the beat, and the balance between the beat and the background music in the mixing script. These can be adjusted in the script's parameters.
