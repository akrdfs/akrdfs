import numpy as np
import matplotlib.pyplot as plt
def sin_wave(amp, freq, time):
  return amp * np.sin(2*np.pi*freq*time)
time = np.arange(0, 10, 0.001)
sin1 = sin_wave(1, 2, time)
sin2 = sin_wave(2, 5, time)
sin3 = sin_wave(4, 1, time)
plt.figure(figsize=(12,5))
plt.plot(time, sin1)
plt.plot(time, sin2)
plt.plot(time, sin3)
plt.axis([0, 5, -5, 5])
plt.grid(True)
plt.xlabel('Second [s]')
plt.ylabel('Amplitude [m]')
plt.title('sin1,sin2,sin3')
sin_sum = sin1 + sin2 + sin3
plt.figure(figsize=(12,5))
plt.plot(time, sin_sum)
plt.grid(True)
plt.title('sin_sum')
plt.show()
dt = 0.001 
Fs = 1/dt
len_data = len(sin_sum)
n = np.arange(len_data)
T = len_data/Fs
freq = n/T
Y_raw = np.fft.fft(sin_sum)/len_data
plt.figure(figsize=(12,5))
plt.stem(freq, np.abs(Y_raw)*2)
plt.axis([0, 15, 0, 5])
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [m]')
plt.grid(True)
plt.title('FFT')
y = np.fft.ifft(Y_raw)*len_data
plt.figure(figsize=(12,5))
plt.plot(time, y)
plt.axis([0, 10, -10, 10])
plt.grid(True)
plt.xlabel('Second [s]')
plt.ylabel('Amplitude [m]')
plt.title('iFFT')# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""





