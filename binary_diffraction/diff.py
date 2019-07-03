import numpy as np

def sim_diff_1D(domain_unit,domain_boundary,cdf,domain_size = 2**10,domain_number = 2**10): 
    Hist = np.zeros(np.size(cdf))
    Int = 0
    H = np.linspace(0,1,domain_size+1)
    H = np.delete(H,domain_size)
    for x in range(0, domain_number-1):
        domain = np.array([])
        
        while np.size(domain) <= domain_size-1:
            tmp = cdf - np.random.rand(1,1)
            tmp[tmp<0] = float("inf")
            
            index = np.argmin(tmp)

            index_tmp = 0
            for y in range(0, index):
                domain = np.append(domain,domain_unit)
                index_tmp += 1
            if index_tmp > 0:
                Hist[index_tmp] = Hist[index_tmp] + 1
            
            domain = np.append(domain,domain_boundary)            

        domain = np.delete(domain,range(domain_size,domain.size))
        Ifft = np.fft.fft(domain)
        Int = Int + np.abs(Ifft)**2
#        np.disp(x/(domain_number-1))
    Int = Int/(domain_number*domain_size)
    Hist = Hist/np.sum(Hist)
    return Int,H,Hist

def sim_diff_2D(domain_unit,cdf_length,cdf_domain_unit,domain_size = 2**10,domain_number = 2**10):
    
    Int = 0
    
    for x in range(0, domain_number):
        print((x+1)/domain_number)
        domain = np.zeros((domain_size,domain_size))
        
        domain_unit_index = np.random.randint(0,len(domain_unit)-1)

        domain_index = 0
        while domain_index < domain_size:
            # whats the size of the domain_unit?
            tmp = cdf_length[domain_unit_index] - np.random.rand(1,1)
            tmp[tmp<0] = float("inf")
            
            index = np.argmin(tmp)
            domain_tmp = np.repeat(domain_unit[domain_unit_index],index,axis=1)
            
            index_length = index*np.shape(domain_unit[domain_unit_index])[1]
            
            # insert the domain_unit into the domain
            if domain_index+index_length <= domain_size:
                domain[:,domain_index:domain_index+index_length] = domain_tmp
            else:
                domain[:,domain_index:] = domain_tmp[:,:-(domain_index+index_length-domain_size)]
            # set the domain_index to the new position
            domain_index = domain_index + index_length

            #whats the next domain_unit gonna be?            
            domain_unit_index_tmp = domain_unit_index
            while domain_unit_index == domain_unit_index_tmp:
                tmp = cdf_domain_unit - np.random.rand(1,1)
                tmp[tmp<0] = float("inf")
            
                domain_unit_index_tmp = np.argmin(tmp)
            domain_unit_index = domain_unit_index_tmp
        # calculate the diffraction pattern of the domain    
        Ifft = np.fft.fft2(domain)
        # add the diffraction patterns of the different domains (incoherently)
        Int = Int + np.abs(Ifft)**2
    # average over all the different domains
    Int = Int/domain_number
    return Int, domain
