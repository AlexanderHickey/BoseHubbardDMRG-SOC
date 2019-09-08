#!/bin/bash
#SBATCH --account=def-feder
#SBATCH --time=10:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=5G
#SBATCH --mail-user=alexander.hickey@ucalgary.ca
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL

module load miniconda2
python __runALPS.py runtest 32 0.41 0.5 0.6 0.55 0.25 0.0
