import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.io import wavfile

import os
dir = os.path.dirname(os.path.realpath(__file__))

import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

def normalize01(data):
    data -= np.amin(data)
    data /= np.amax(data)

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
print("rate = " + str(rate))

data = normalizeByDType(data)
if(len(data.shape)>1):
    data = data[:,0] # make mono

f, t, spect = signal.stft(data, window='tukey')
plt.figure()
plt.pcolormesh(t/rate, f, np.abs(spect), shading='gouraud')
plt.ylim([f[1], f[-1]])
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.yscale('log')
plt.show()

spect = np.stack([np.real(spect), np.imag(spect), np.zeros(spect.shape)], 2)
normalize01(spect)
# spect = np.real(np.abs(spect))

plt.imsave(dir + '/' + 'spect.bmp', spect)