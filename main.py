from src.dataLoader import load_iq_samples
from src.gui import plotSpectrogram

# File path and parameters
file_path = './data/output.csv'
sample_rate = 50e6
nfft = 4096

# Load IQ samples
iq_samples = load_iq_samples(file_path)

# Plot the spectrogram
plotSpectrogram(iq_samples, sample_rate, nfft)