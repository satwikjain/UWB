from src.dataLoader import load_iq_samples
from src.gui import plotSpectrogram, plotIQdata, plotFFT
from src.fftProcessor import process_iq_samples, save_fft_results_to_csv
from src.frequencyDetector import getFrequencyAboveThreshold, getCentreFrequencies
from src.pulseAnalysis import group_frequencies


# File path and parameters
file_path = './data/output.csv'
sample_rate = int(50e6)
nfft = 4096
threshold = 87

# Load IQ samples
iq_samples = load_iq_samples(file_path)

# plotIQdata(iq_samples)

# plotFFT(4, iq_samples, sample_rate, nfft)

fft_results = process_iq_samples(iq_samples, sample_rate, nfft)

frequenciesAboveThreshold, fftModifiedResults = getFrequencyAboveThreshold(threshold, fft_results, nfft, sample_rate)

centerFrequencies = getCentreFrequencies(1, frequenciesAboveThreshold)

a = group_frequencies(fftModifiedResults, centerFrequencies)

print(a)
# csv_filename = './data/peakFrequencyArray.csv'
# save_fft_results_to_csv(fftModifiedResults, csv_filename)