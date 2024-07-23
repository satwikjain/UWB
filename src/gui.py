import matplotlib.pyplot as plt
import numpy as np
from src.fftProcessor import getFFTMagnitude

def plotSpectrogram(iq_samples, sample_rate, nfft=4096, cmap='viridis'):
    """
    Plot a waterfall spectrogram of IQ samples.

    Parameters:
    iq_samples (numpy array): The IQ samples.
    sample_rate (float): The sample rate in Hz.
    nfft (int): The number of points in each FFT. Default is 4096.
    cmap (str): The colormap to use for the spectrogram. Default is 'viridis'.
    """
    plt.specgram(iq_samples, NFFT=nfft, Fs=sample_rate, noverlap=nfft//2, cmap=cmap)
    
    # Convert frequency axis to MHz
    ax = plt.gca()
    y_labels = ax.get_yticks()
    ax.set_yticklabels(y_labels / 1e6)
    
    # Set plot labels and title
    plt.xlabel("Time [s]")
    plt.ylabel("Frequency [MHz]")
    plt.title("Waterfall Spectrogram of IQ Samples")
    plt.colorbar(label="Intensity [dB]")
    plt.show()


def plotIQdata(iq_samples):
    # Compute the magnitude of the complex samples
    magnitude = np.abs(iq_samples)
    
    # Plot the magnitude vs time
    plt.plot(magnitude)
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.title("Time Domain Amplitude of IQ Samples")
    plt.show()


def plotFFT(i, samples, sample_rate, n_samples):
    spect = getFFTMagnitude(i, samples, sample_rate, n_samples)
    freqs = np.fft.fftshift(np.fft.fftfreq(n_samples, 1 / sample_rate))
    plt.plot(freqs, spect)
    plt.xlabel("Frequency [MHz]")
    plt.ylabel("Amplitude [dB]")
    plt.show()
    
