import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import rfft, irfft
from scipy.io import wavfile

import os
dir = os.path.dirname(os.path.realpath(__file__))

import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
input1_file = filedialog.askopenfilename()
input2_file = filedialog.askopenfilename()

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

rate, input1 = wavfile.read(input1_file)
input1 = normalizeByDType(input1)
if(len(input1.shape)>1):
    input1 = input1[:,0] # make mono

rate, input2 = wavfile.read(input2_file)
input2 = normalizeByDType(input2)
if(len(input2.shape)>1):
    input2 = input2[:,0]

nsamples = min(input2.size,input1.size)

outspect = rfft(input1,nsamples) * rfft(input2,nsamples) # convolve
output = irfft(outspect)
wavfile.write(dir + '/' + 'output.wav', rate, output)

# plot amplitudes
fig, ((ax1, ax2, ax3)) = plt.subplots(1, 3, sharey=True)
fig.set_figwidth(20)
ax1.plot(input1)
ax2.plot(input2)
ax3.plot(0.5*output)
plt.show()

