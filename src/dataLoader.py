import pandas as pd
import numpy as np
import csv

def load_iq_samples(file_path, num_samples=500000):
    data = pd.read_csv(file_path, nrows=num_samples)
    
    I_samples = data['I'].values
    Q_samples = data['Q'].values
    
    complex_samples = I_samples + 1j * Q_samples
    
    return complex_samples
