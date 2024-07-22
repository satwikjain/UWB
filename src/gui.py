import matplotlib.pyplot as plt

def plotSpectrogram(iq_samples, sample_rate, nfft=4096, cmap='viridis'):
    """
    Plot a waterfall spectrogram of IQ samples.

    Parameters:
    iq_samples (numpy array): The IQ samples.
    sample_rate (float): The sample rate in Hz.
    nfft (int): The number of points in each FFT. Default is 4096.
    cmap (str): The colormap to use for the spectrogram. Default is 'viridis'.
    """
    plt.specgram(iq_samples, NFFT=nfft, Fs=sample_rate/1e6, noverlap=nfft//2, cmap=cmap)
    
    # Set plot labels and title
    plt.xlabel("Time [s]")
    plt.ylabel("Frequency [MHz]")
    plt.title("Waterfall Spectrogram of IQ Samples")
    plt.colorbar(label="Intensity [dB]")
    plt.show()