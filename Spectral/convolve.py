import math
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
print(nsamples)

fs = 1

f1, t1, outspect1 = signal.stft(input1,fs) 
f2, t2, outspect2 = signal.stft(input2,fs)
print("t1 = " + str(t1))
print("t2 = " + str(t2))
outspect1 = outspect1[:,:min(outspect1.shape[1],outspect2.shape[1])]
outspect2 = outspect2[:,:min(outspect1.shape[1],outspect2.shape[1])]
outspect = outspect1 * outspect2 * 100
t, output = signal.istft(outspect, fs)

# outspect = rfft(input1,nsamples) * rfft(input2,nsamples) # convolve
# output = irfft(outspect)
wavfile.write(dir + '/' + 'output.wav', rate, output)

# plot amplitudes
fig, ((ax1, ax2, ax3)) = plt.subplots(1, 3, sharey=True)
fig.set_figwidth(20)
ax1.plot(input1)
ax2.plot(input2)
ax3.plot(0.5*output)
plt.show()

