BoseHubbardDMRG-SOC
==========
This is a Python package used to simulate a one-dimensional extended Bose-Hubbard model with spin orbit coupling using Density Matrix Renormalization Group (DMRG). The ALPS DMRG algorithm with periodic boundary conditions is implemented. This package supports the submission of independent simulations to a computing cluster.

## Standard use:

* Edit the preamble of the master.py file to set simulation parameters and the corresponding list of sweep variables.
* \_\_runALPS.py compiles and executes the ALPS simulation. The preamble contains information about the Fock basis trunction and the number of states kept in each DMRG sweep.
* \_\_process\_data.py is used to sweep through the simulation output files, and generates plots of the correlations using the ploy.py file.
* sample\_script.sh is an example of the shell file used to submit jobs to a Compute Canada cluster.

## Requirements

* Python 2.7.x
* ALPS 2.3.0, if using the conda installer, create an environment first to avoid complications with the PATH variable. For example, run:

      conda create --name myenv python=2.7
      conda activate myenv
      conda config --add channels conda-forge 
      conda install alps
      
