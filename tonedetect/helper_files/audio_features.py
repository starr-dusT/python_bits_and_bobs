import librosa
import matplotlib.pyplot as plt
import librosa.display
import csv
import numpy as np


file = open('../train_set_512.csv', 'w')
with file:
    writer = csv.writer(file)
    #writer.writerow('All, but last row are features. Last row is truth data')

number_of_samps = 8834
fig, ax = plt.subplots()
mode = 0

for i in np.arange(number_of_samps):
    # Load Audio File
    audio_path = '../training_samples/samp_' + str(i) + '.wav'
    x, sr = librosa.load(audio_path, duration=1)

    feature_row = []
    stft = np.abs(librosa.stft(x, n_fft=512, hop_length=256, win_length=512))
    bin_avg_stft = []
    [bin_avg_stft.append(np.mean(stft_row)) for stft_row in stft]
    normal_stft = bin_avg_stft/max(bin_avg_stft)

    for normal_stft_i in normal_stft:
        feature_row.append(normal_stft_i)


    ax.plot(feature_row)

    if mode == 0:
        feature_row.append(1)
        mode = 1
    elif mode == 1:
        feature_row.append(2)
        mode = 2
    elif mode == 2:
        feature_row.append(3)
        mode = 3
    else:
        feature_row.append(4)
        mode = 0


    file = open('../train_set_512.csv', 'a')
    with file:
        writer = csv.writer(file)
        writer.writerow(feature_row)

plt.show()
