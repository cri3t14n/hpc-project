#!/bin/bash
#BSUB -J wallheat_dynamic_all
#BSUB -q hpc
#BSUB -n 10
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=4096]"
#BSUB -W 08:00
#BSUB -o /zhome/aa/6/205647/hpc-project/Mini-Project/outputs/dynamic_all_%J.out
#BSUB -e /zhome/aa/6/205647/hpc-project/Mini-Project/errors/dynamic_all_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

for W in 1 2 4 5 10
do
    echo "===== workers=$W ====="
    python simulate_dynamic.py 50 $W
    echo
done