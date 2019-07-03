from binary_diffraction.cdf import cdf
from binary_diffraction.diff import sim_diff_1D
import numpy as np
#import matplotlib.pyplot as plt
#from scipy.stats import gamma

def main():
    domain_unit = np.array([1,0])
    domain_boundary = np.array([0])
    cdf_ = cdf()
    
    Int,H,Hist = sim_diff_1D(domain_unit,domain_boundary,cdf_)
    with open('test.txt','w') as file:
        file.writelines('{0}'.format(Int))
