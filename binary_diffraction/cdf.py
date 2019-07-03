import numpy as np

def cdf():
    pdf = np.array([1,2,3,4,5])
    pdf = pdf/np.sum(pdf)
    cdf = np.cumsum(pdf)
    return cdf

