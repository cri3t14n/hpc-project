#!/bin/bash
#BSUB -J wallheat_numba
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=4096]"
#BSUB -W 04:00
#BSUB -o /zhome/aa/6/205647/hpc-project/Mini-Project/outputs/numba_%J.out
#BSUB -e /zhome/aa/6/205647/hpc-project/Mini-Project/errors/numba_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

/usr/bin/time -p python simulate_numba.py 10