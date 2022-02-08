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

def normalize(data):
    data /= max(np.amax(data), abs(np.amin(data)))
    return data

fs = 1
rate = 44100
data = plt.imread(file_path)
print(data.shape)
data = data[:,:,0] + 1j * data[:,:,1]

tout, dataout = signal.istft(data, fs)
dataout = normalize(dataout)

# plt.figure()
# plt.plot(tout/rate,dataout)
# plt.ylim([-1, 1])
# plt.xlabel('Time [sec]')
# plt.ylabel('Signal')
# plt.show()

# make stereo
dataout = np.stack([dataout,dataout],1)

wavfile.write(dir + '/' + 'output.wav', rate, dataout)

