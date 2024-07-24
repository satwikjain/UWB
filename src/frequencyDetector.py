import numpy as np


def getFrequencyAboveThreshold(threshold: float, fft_results: np.array, n_samples, sample_rate):
    freqs = np.fft.fftshift(np.fft.fftfreq(n_samples, 1 / sample_rate))
    fftModifiedResults = fft_results.copy()
    frequenciesAboveThreshold = []
    for fft_row in fftModifiedResults:
        for i in range(n_samples):
            if fft_row[i] >= threshold:
                frequenciesAboveThreshold.append(freqs[i]/1e6)
                fft_row[i] = freqs[i]/1e6
            else:
                fft_row[i] = 0
    return frequenciesAboveThreshold, fftModifiedResults


def getCentreFrequencies(threshold: int, frequenciesAboveThreshold: list):
    centreFrequencies = []
    sorted_frequencies = np.sort(frequenciesAboveThreshold)
    
    for i in range(1, len(sorted_frequencies)):
        count = 0
        totalsum = sorted_frequencies[0]
        if sorted_frequencies[i] - sorted_frequencies[i - 1] <= threshold:
            totalsum += sorted_frequencies[i]
            count += 1
        else:
            centreFrequencies.append(totalsum//count)
            totalsum = 0
            count = 0
    if count:
        centreFrequencies.append(totalsum//count)
        totalsum = 0
        count = 0
    
    return centreFrequencies


def getPowerAtCentreFreqs(center_frequencies, fft_results, fs, nfft):
    # Frequency and time resolution
    freq_resolution = fs / nfft
    
    powerAtCentreFreq = []
    
    for center_freq in center_frequencies:
        center_freq_hz = round(center_freq) * 1e6  # Convert to Hz
        ind = (nfft // 2) + round(center_freq_hz / freq_resolution)  # Calculate the approximate index      

        if 0 <= ind < nfft:
            # Access the magnitude spectrum at the approximated index and find the max value
            center_freq_magnitude = np.max(fft_results[:, ind])
            powerAtCentreFreq.append(center_freq_magnitude)
            
        else:
            # Handle out-of-range index
            powerAtCentreFreq.append(float('-inf')) 

    
    return powerAtCentreFreq