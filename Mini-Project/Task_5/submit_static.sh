#!/bin/bash
#BSUB -J wallheat_static_all
#BSUB -q hpc
#BSUB -n 25
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=1024]"
#BSUB -W 08:00
#BSUB -o /zhome/aa/6/205647/hpc-project/Mini-Project/outputs/wallheat_static_all_%J.out
#BSUB -e /zhome/aa/6/205647/hpc-project/Mini-Project/errors/wallheat_static_all_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

for W in 25 
do
    echo "===== workers=$W ====="
    python simulate_static.py 50 $W
    echo
done