#  _         _                     
# | |_  ___ | |_  __ _  _ __  _ __ 
# | __|/ __|| __|/ _` || '__|| '__|
# | |_ \__ \| |_| (_| || |   | |   
#  \__||___/ \__|\__,_||_|   |_|   
# 
# Description: Implementation of program to add tone randomly over
#              an audio file. In this case cockpit noise from a 747.
# Author: Tyler Starr
# Date Created: 23 April 2020
# https://github.com/starr-dusT/*need to add*

# Import needed libraries
import librosa
import numpy as np
from scipy.io.wavfile import write
import random
import matplotlib.pyplot as plt

def generate_tone(Fs, f_tone, samples_tone, volume_tone):
    tone_x = np.arange(samples_tone) 
    tone = volume_tone*np.sin(2 * np.pi * f_tone * tone_x / Fs)
    return tone


# Import base audio file
audio_data, Fs = librosa.load('cockpit_audio.wav', sr=None)
# Get length of clip in seconds
time_length = int(len(audio_data)/Fs)

# Split audio file
num_splits = int(5*time_length)
audio_data_split = np.array_split(audio_data,num_splits)
f_tone = [500,750,1000]

for i in range(0,num_splits-2,4):
    audio_data_split[i] += generate_tone(Fs, f_tone[0], len(audio_data_split[i]), random.uniform(0.02,0.1))
    audio_data_split[i+1] += generate_tone(Fs, f_tone[1], len(audio_data_split[i+1]), random.uniform(0.02,0.1))
    audio_data_split[i+2] += generate_tone(Fs, f_tone[2], len(audio_data_split[i+2]), random.uniform(0.02, 0.1))
    


# Define different tones we will look for (Hz)
# Define possible lengths in time (0.1-5s)
#time_tones = np.arange(5,51,1)

# Define the number of splits (like sample period) to be 0.1s
#num_splits = int(10*time_length)
# Scale sine wave and remove sine wave in waveform alternately
#audio_data_split = np.array_split(audio_data,num_splits)
# Define the number of each tone to place in output
#num_each_tone = 20
# possible times
#possible_indexes = np.arange(0,num_splits,1)

#for f_tone in f_tones: 
#    total_tones = []
#    for i in range(num_each_tone):
#        start_tone = possible_indexes[random.randint(0,len(possible_indexes))]
#        tone_length = time_tones[random.randint(0,len(time_tones)-1)]
#        total_tone = np.arange(start_tone, start_tone+tone_length, 1)
#        total_tones.extend(total_tone)
#        possible_indexes = np.delete(possible_indexes,total_tone)


#    # Loop through split audio data
#    for index in total_tones:
#        audio_data_split[index] += generate_tone(Fs, f_tone, 0.2, 0.05)[:len(audio_data_split[index])]
#        print(index)

for i in np.arange(len(audio_data_split)):
    scaled = np.int16(audio_data_split[i]/np.max(np.abs(audio_data_split[i])) * 32767)
    write('../training_samples/samp_' + str(i) + '.wav', 44100, scaled)

