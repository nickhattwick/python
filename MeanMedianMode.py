import numpy as np
from scipy import stats

def mmm(x):
    return np.mean(x) #calculates mean
    return np.median(x) #calculates median
    return stats.mode(x) #calculates mode
