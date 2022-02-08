import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import scipy
from scipy.io import wavfile
from scipy import ndimage, misc

import os
dir = os.path.dirname(os.path.realpath(__file__))

import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

def normalize(data):
    data /= max(np.amax(data), abs(np.amin(data)))
    return data

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

fs = 1

f, t, spect = signal.stft(data, fs, window='tukey')
plt.figure()
plt.pcolormesh(t/rate, f, np.abs(spect), shading='gouraud')
plt.ylim([f[1], f[-1]])
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.yscale('log')
plt.show()

# Do what you wish with the ndarray of spectral values
# spect = np.where(np.abs(spect) >= 1/100, spect, 0)
# spect = spect**0.5
# spect = spect**3

spect = np.real(spect)

for i in range(1):
    # weights = np.array([[0,0,0],[10,10,10],[0,0,0]])
    # spect = ndimage.convolve(spect,weights)

    spect = ndimage.grey_dilation(np.real(spect),1)
    # spect = ndimage.grey_erosion(np.real(spect),1)
    # spect = ndimage.grey_closing(np.real(spect),30)
    # spect = ndimage.grey_opening(np.real(spect),30)

    # spect = np.hypot(ndimage.sobel(spect,0), ndimage.sobel(spect,1))

    # spect = ndimage.laplace(spect)

    # spect = ndimage.prewitt(spect)

    # spect = ndimage.gaussian_filter(spect,0.1)

    # spect = ndimage.uniform_filter(spect,1)

plt.figure()
plt.pcolormesh(t/rate, f, np.abs(spect), shading='gouraud')
plt.ylim([f[1], f[-1]])
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.yscale('log')
plt.show()

tout, dataout = signal.istft(spect, fs)
dataout = normalize(dataout)

plt.figure()
plt.plot(tout/rate,dataout)
plt.ylim([-1, 1])
plt.xlabel('Time [sec]')
plt.ylabel('Signal')
plt.show()

# make stereo
dataout = np.stack([dataout,dataout],1)

wavfile.write(dir + '/' + 'output.wav', rate, dataout)

