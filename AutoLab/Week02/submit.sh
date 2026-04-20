#!/bin/bash
#BSUB -J BasicNumpy_5
#BSUB -q hpc
#BSUB -n 1
#BSUB -W 00:15
#BSUB -R "rusage[mem=512]"
#BSUB -o ~/hpc-project/batch_outputs/python_%J.out
#BSUB -e ~/hpc-project/batch_errors/python_%J.err

# Initialize Python environment
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

# Run Python script
python BasicNumpy_5.py ./input.npy 10