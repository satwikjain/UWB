import numpy as np
import pandas as pd

def getFFTMagnitude(i, samples, sample_rate, n_samples):
    spect = np.fft.fftshift(np.fft.fft(samples[n_samples * i: n_samples * (i + 1)]))
    return 20 * np.log10(abs(spect))


def process_iq_samples(iq_samples, sample_rate, chunk_size):
    n_chunks = len(iq_samples) // chunk_size
    fft_results = []

    for i in range(n_chunks):
        fft_magnitude = getFFTMagnitude(i, iq_samples, sample_rate, chunk_size)
        fft_results.append(fft_magnitude)
    
    return np.array(fft_results)


def save_fft_results_to_csv(fft_results, filename):
    df = pd.DataFrame(fft_results)
    df.to_csv(filename, index=False, header=False)

