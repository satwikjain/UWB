import numpy as np
import pandas as pd

def getFFTMagnitude(i, samples, sample_rate, n_samples):
    spect = np.fft.fftshift(np.fft.fft(samples[n_samples * i: n_samples * (i + 1)]))
    
    # Compute the power spectrum (magnitude squared)
    power_spectrum = np.abs(spect)**2
    
    # Normalize the power spectrum
    power_spectrum /= n_samples

    # Convert to dBm: 10 * log10(power / 1mW)
    power_spectrum_dbm = 10 * np.log10(power_spectrum / 1e-3)
    
    return power_spectrum_dbm



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

