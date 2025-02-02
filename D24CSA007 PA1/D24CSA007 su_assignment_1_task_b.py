# -*- coding: utf-8 -*-
"""SU Assignment 1 Task-B.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jsfzBg0Tff0QUyrgQFELS-0ExSHG_Urr
"""

import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal

def compute_spectrogram(audio_path, window='hann', n_fft=2048, hop_length=512):
    y, sr = librosa.load(audio_path, sr=None)
    S = librosa.stft(y, n_fft=n_fft, hop_length=hop_length, window=window)
    S_db = librosa.amplitude_to_db(np.abs(S), ref=np.max)
    return S_db, sr

def plot_spectrograms(audio_files, labels, window='hann'):
    plt.figure(figsize=(12, 10))

    for i, (audio_path, label) in enumerate(zip(audio_files, labels)):
        S_db, sr = compute_spectrogram(audio_path, window=window)
        plt.subplot(2, 2, i+1)
        librosa.display.specshow(S_db, sr=sr, hop_length=512, x_axis='time', y_axis='log')
        plt.colorbar(format='%+2.0f dB')
        plt.title(f"Spectrogram - {label} ({window} Window)")

    plt.tight_layout()
    plt.show()

audio_files= ["classical.wav", "rock.wav", "edm.wav", "pop.wav"]
labels= ["Classical", "Rock", "EDM", "Pop"]

# Plot spectrograms
plot_spectrograms(audio_files, labels)