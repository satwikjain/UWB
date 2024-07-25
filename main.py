from src.dataLoader import load_iq_samples
from src.gui import plotSpectrogram, plotIQdata, plotFFT, print_detected_frequencies
from src.fftProcessor import process_iq_samples, save_fft_results_to_csv
from src.frequencyDetector import getFrequencyAboveThreshold, getCentreFrequencies, getPowerAtCentreFreqs
from src.pulseAnalysis import group_frequencies, getPulseWidthAndDuration


# File path and parameters
file_path = './data/output.csv'
sample_rate = int(50e6)
nfft = 4096
threshold = 85

# Load IQ samples
iq_samples = load_iq_samples(file_path)

# plotSpectrogram(iq_samples, sample_rate, nfft=4096, cmap='viridis')
# plotIQdata(iq_samples)


# plotFFT(6, iq_samples, sample_rate, nfft)

fft_results = process_iq_samples(iq_samples, sample_rate, nfft)

frequenciesAboveThreshold, fftModifiedResults = getFrequencyAboveThreshold(threshold, fft_results, nfft, sample_rate)

centerFrequencies = getCentreFrequencies(1, frequenciesAboveThreshold)

positionForCentreFreq = group_frequencies(fftModifiedResults, centerFrequencies)

pulseWidthAndDuration = getPulseWidthAndDuration(positionForCentreFreq, nfft, sample_rate)

powerAtCentreFreq = getPowerAtCentreFreqs(centerFrequencies, fft_results, sample_rate, nfft)

print_detected_frequencies(centerFrequencies, pulseWidthAndDuration, powerAtCentreFreq)


# csv_filename = './data/peakFrequencyArray.csv'
# save_fft_results_to_csv(fftModifiedResults, csv_filename)