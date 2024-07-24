import numpy as np

def group_frequencies(arr, center_frequencies, threshold=1e6):
    """
    Group frequencies in a 2D array that are within a given threshold of center frequencies.

    Parameters:
    arr (list of lists): 2D array of frequencies.
    center_frequencies (list): List of center frequencies.
    threshold (float): Threshold value to group frequencies. Default is 1 MHz (1e6).

    Returns:
    list of lists: 2D list where each element is a list of indices from the input array.
    """
    # Initialize list to store coordinates
    a = [[] for _ in range(len(center_frequencies))]

    for p in range(len(center_frequencies)):
        for i in range(len(arr[0])):
            for j in range(len(arr)):
                # Check the condition and append the index
                if abs(arr[j][i] - center_frequencies[p]) <= threshold and arr[j][i] != 0:
                    a[p].append(j)

    return a


def getPulseWidth(positionForCentreFreq, n_samples, sample_rate):
    """
    Calculate the pulse width for each center frequency.

    Parameters:
    positionForCentreFreq (list of lists): List containing positions of center frequencies.
    n_samples (int): Number of samples.
    sample_rate (float): Sample rate.

    Returns:
    list: Pulse width for each center frequency in Micro Second.
    """
    pulseWidthForCentreFreq = []
    for currentCentreFreq in positionForCentreFreq:
        maxi = 0
        currentPosition = currentCentreFreq[0]
        count = 1
        for i in range(1, len(currentCentreFreq)):
            if currentCentreFreq[i] == currentPosition + 1:
                count += 1
                maxi = max(maxi, count)
            else:
                count = 1
            currentPosition = currentCentreFreq[i]
        pulseWidthForCentreFreq.append(maxi)
    
    factor = (n_samples / sample_rate) * 1e6
    
    # Multiply each element in pulseWidthForCentreFreq by the factor to calculate Time of PulseWidth in Micro Second
    pulseWidthForCentreFreq = [width * factor for width in pulseWidthForCentreFreq]
    
    return pulseWidthForCentreFreq