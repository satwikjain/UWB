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