from src.dataLoader import load_iq_samples
from src.gui import plotSpectrogram, plotIQdata, plotFFT
from src.fftProcessor import process_iq_samples, save_fft_results_to_csv

# File path and parameters
file_path = './data/output.csv'
sample_rate = 50e6
nfft = 4096

# Load IQ samples
iq_samples = load_iq_samples(file_path)

# Plot the spectrogram
# plotSpectrogram(iq_samples, sample_rate, nfft)

plotIQdata(iq_samples)


plotFFT(6, iq_samples, int(50e6), 4096)

# Process the IQ samples in chunks and get the FFT results
fft_results = process_iq_samples(iq_samples, sample_rate, 4096)

# Convert the FFT results to binary based on the condition
binary_fft_results = (fft_results >= 90).astype(int)

# Save the binary FFT results to a CSV file
csv_filename = './data/binary_fft_output.csv'
save_fft_results_to_csv(binary_fft_results, csv_filename)

# Optionally, print the binary FFT results
print(binary_fft_results)
