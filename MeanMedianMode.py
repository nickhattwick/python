import numpy as np #for median and mean
from scipy import stats #for mode

def mmm(x):
    return np.mean(x) #calculates mean
    return np.median(x) #calculates median
    return stats.mode(x) #calculates mode
