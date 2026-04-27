#!/bin/bash
#BSUB -J wallheat_all
#BSUB -q c02613
#BSUB -n 4
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=8GB]"
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -W 00:30
#BSUB -o /zhome/aa/6/205647/hpc-project/Mini-Project/outputs/wallheat_all_%J.out
#BSUB -e /zhome/aa/6/205647/hpc-project/Mini-Project/errors/wallheat_all_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

python ../Task_10/simulate_cupy_fixed.py 4571 > all_floorplans_cupy_raw.csv