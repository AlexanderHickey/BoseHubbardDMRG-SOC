# -*- coding: utf-8 -*-
"""
@author: Alex Hickey

This module is used to submit multiple tasks to a Compute Canada cluster, by
sweeping over a specified parameter and keeping the others fixed.

Note that submitting values of the spin-orbit coupling parameter gamma
that do not lie in the Brillouin zone of the discrete lattice can
lead to convergence issues.
"""
import numpy as np
import os, subprocess
import sys


L = 64 #Length of chain
t, mu, V, Uud, hz, gamma = 0.45, 0.5, 1.00, 0.6, 0.25, np.pi/2-np.pi/L
X = 'gamma' #Coarse grained sweep variable
Xmin, Xmax = 0.0,np.pi #Set bounds on sweep variable, inclusive
Npnts = L/2 #Number of data points
time = '240:00:00' #Maximum run time
memory = '7G' #Memory per core required, this is NOT shared between jobs!!!
start_indx = 820 #Index to label resulting data files
email = 'alexander.hickey@ucalgary.ca'

#Index parameter set
par = [t,mu,V,Uud,hz,gamma]
par_indx = {"t":0,"mu":1,"V":2,"Uud":3,"hz":4,"gamma":5}

#Set appropriate sweep function.
Xlist = np.linspace(Xmin,Xmax,Npnts)

#Preamble to submit compute canada job
preamble = ["#!/bin/bash\n",
            "#SBATCH --account=def-feder\n",
            "#SBATCH --time={}\n".format(time),
            "#SBATCH --nodes=1\n",
            "#SBATCH --ntasks=1\n",
            "#SBATCH --mem={}\n".format(memory),
            "#SBATCH --mail-user={}\n".format(email),
            "#SBATCH --mail-type=FAIL\n",
            "\n",
            "module load miniconda2\n"]

def execute(x0,filename,read = False):
    '''
    Generates shell files to submit a single parameter set as
    single processor job.
    '''
    
    global par
    
    #Update global parameter list
    par[par_indx[X]] = x0
    
    #Generate shell file
    with open('run.sh','w') as shell:

        shell.write("".join(preamble))
        shell.write("python __runALPS.py {} {} {} {} {} {} {} {}".format(filename,L,*par))
        
    #Print out contents of shell file
    if read:
        with open('run.sh','r') as file:    
            print(file.read())
    
    #Submit job to scheduler
    #Note: subprocess in Python 2.7 does not print terminal output
    subprocess.check_output(['sbatch run.sh'], shell=True)
    
    #Delete shell file
    os.remove('run.sh')


def main():
    '''
    Iterate through parameter set and submit each job
    '''
    
    #Set starting index
    indx = start_indx
    
    #Iterate through parameter set
    for x0 in Xlist:
    
        execute(x0,indx)
        indx += 1

if __name__ == '__main__':
 
    main()        

