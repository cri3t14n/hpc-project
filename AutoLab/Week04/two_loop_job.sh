#!/bin/bash
#BSUB -J haversine
#BSUB -q hpc
#BSUB -n 1
#BSUB -W 00:15
#BSUB -R "rusage[mem=2048]"
#BSUB -R "select[model == XeonGold6126]"
#BSUB -o /zhome/aa/6/205647/hpc-project/batch_outputs/haversine_%J.out
#BSUB -e /zhome/aa/6/205647/hpc-project/batch_errors/haversine_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python haversine.py input.csv