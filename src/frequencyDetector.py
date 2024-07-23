import numpy as np


def getPeakFrequencyArrays(threshold, fft_results, n_samples, sample_rate):
    freqs = np.fft.fftshift(np.fft.fftfreq(n_samples, 1 / sample_rate))
    frequenciesAboveThreshold = []
    for fft_row in fft_results:
        for i in range(n_samples):
            if fft_row[i] >= threshold:
                frequenciesAboveThreshold.append(freqs[i]/1e6)
                fft_row[i] = freqs[i]/1e6
            else:
                fft_row[i] = 0
    return frequenciesAboveThreshold, fft_results


def getCentreFrequencies(threshold, frequenciesAboveThreshold):
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
