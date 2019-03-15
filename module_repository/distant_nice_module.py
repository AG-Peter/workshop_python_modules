# function
def nice_function(text):
    print("Given text is    '{}''".format(text.upper()))
    
    out = text[::-1].upper()
    print("Inverted text is '{}'".format(out))
    return out

# dictionary which maps AS 3 letter to 1 letter code 
nice_dictionary = {
    'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
    'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
    'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
    'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'
}

# numpy array loaded from file
import numpy as np
nice_data = np.loadtxt("reference.dat")