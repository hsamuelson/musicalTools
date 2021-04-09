import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft
from scipy.io import wavfile

import os
dir = os.path.dirname(os.path.realpath(__file__))

import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()


def normalizeByDType(data):
    if(data.dtype == np.dtype('uint8')):
        bitcount = 8
    elif(data.dtype == np.dtype('int16')):
        bitcount = 16
    elif(data.dtype == np.dtype('int32')):
        bitcount = 32
    elif(data.dtype == np.dtype('float32')):
        bitcount = 1
    else:
        bitcount = 16
    data = (data / 2**(bitcount-1)) # normalize to -1 to 1
    return data


rate, data = wavfile.read(file_path)

data = normalizeByDType(data)
if(len(data.shape)>1):
    data = data[:,0] # make mono

# plot amplitudes
plt.plot(data)
plt.ylim((-1.,1.))
plt.show()

window_size = 2**10
stride = int(window_size/2**5)
wps = rate/stride # windows/second
spect = np.empty([int(data.shape[0]/stride),window_size])

for i in range(spect.shape[0]):
    spect[i] = fft(data[i*stride:],window_size)

# plot spectrogram
plt.imshow(np.abs(spect.T[:int(window_size/2)]), cmap='bone', interpolation='none', aspect='auto', vmin=0.0, vmax=1.0, origin='lower')
plt.xlabel('windows')
plt.ylabel('frequency [Hz]')
plt.show()

# convert spectrogram back to sound
outdata = np.zeros(data.shape[0])
for i in range(spect.shape[0]):
    outdata[(i*stride):min(data.shape[0],i*stride+window_size)] += np.abs(ifft(spect[i]))[:min(window_size,data.shape[0]-i*stride)]

wavfile.write(dir + '/' + 'output.wav', rate, outdata)

