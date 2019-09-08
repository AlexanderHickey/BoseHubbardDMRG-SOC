'''
This module is used to compute the ground state properties
of the model using the ALPS DMRG algorithm. 
'''

import pyalps
import numpy as np
import sys

open_chain = False #Set false for periodic boundary conditions
Nmax = 3 #Maximum number of bosons per site per spin type
sweeps = 2 #Number of DMRG sweeps
warmup_states = 15 #Number of initial states to grow the DMRG blocks
max_states = 75 #Maximum number of DMRG states kept


#Fetch job details from command line input
filename = sys.argv[1]
L = int(sys.argv[2])
t = float(sys.argv[3])
mu = float(sys.argv[4])
V = float(sys.argv[5])
Uud = float(sys.argv[6])
hz = float(sys.argv[7])
gamma = float(sys.argv[8])
cg, sg = np.cos(gamma), np.sin(gamma)

#Set boundary conditions
if open_chain:
    lattice_type = "open chain lattice"   
else:
    lattice_type = "periodic chain lattice"

#Prepare the input parameters
parms = [ { 
        'LATTICE_LIBRARY'           : "models/BHlattice.xml",
        'MODEL_LIBRARY'             : "models/SOCmodel.xml",
        'LATTICE'                   : lattice_type,
        'MODEL'                     : 'SOC Bose Hubbard',     
        'L'                         : L,
        'NMax'                      : Nmax,
        't'                         : t,
        'mu'                        : mu,
        'V'                         : V,
        'Uud'                       : Uud,
        'hz'                        : hz,
        'cg'                        : cg,
        'sg'                        : sg,
        'SWEEPS'                    : sweeps,
        'NUM_WARMUP_STATES'         : warmup_states,
        'NUMBER_EIGENVALUES'        : 1,
        'MAXSTATES'                 : max_states,
        'MEASURE_LOCAL[nUP]'                          : 'nUP',
        'MEASURE_LOCAL[nDO]'                          : 'nDO',
        'MEASURE_CORRELATIONS[One-body Correlation UP]'   :"bdagUP:bUP",
        'MEASURE_CORRELATIONS[One-body Correlation DO]'   :"bdagDO:bDO",
        'MEASURE_CORRELATIONS[One-body Correlation UPDO]'   :"bdagUP:bDO",
        'MEASURE_CORRELATIONS[Two-body Correlation UP]'   :"nUP:nUP",
        'MEASURE_CORRELATIONS[Two-body Correlation DO]'   :"nDO:nDO",
        'MEASURE_CORRELATIONS[Two-body Correlation UPDO]'   :"nUP:nDO"
       } ]


#Write the input file and run the simulation
input_file = pyalps.writeInputFiles(filename,parms)
res = pyalps.runApplication('dmrg',input_file,writexml=False,MPI=None)

#Load measurements for the ground state
data = pyalps.loadEigenstateMeasurements(pyalps.getResultFiles(prefix=filename))

#Print the properties of the ground state
if __name__ == '__main__':

    for s in data[0]:
        print s.props['observable'], ' : ', s.y[0]






