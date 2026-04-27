#!/bin/bash
#BSUB -J cupy_nsys_fixed
#BSUB -q c02613
#BSUB -n 4
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=8GB]"
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -W 00:30
#BSUB -o /zhome/aa/6/205647/hpc-project/Mini-Project/outputs/cupy_nsys_fixed_%J.out
#BSUB -e /zhome/aa/6/205647/hpc-project/Mini-Project/errors/cupy_nsys_fixed_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

nsys profile -o cupy_profile_fixed_${LSB_JOBID} python simulate_cupy_fixed.py 10
nsys stats cupy_profile_fixed_${LSB_JOBID}.nsys-rep > cupy_profile_fixed_${LSB_JOBID}_stats.txt