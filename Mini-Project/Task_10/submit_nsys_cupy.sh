#!/bin/bash
#BSUB -J cupy_nsys
#BSUB -q c02613
#BSUB -n 4
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=4GB]"
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -W 00:30
#BSUB -o /zhome/aa/6/205647/hpc-project/Mini-Project/outputs/cupy_nsys_%J.out
#BSUB -e /zhome/aa/6/205647/hpc-project/Mini-Project/errors/cupy_nsys_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

nsys profile -o cupy_profile_${LSB_JOBID} python ../Task_9/simulate_cupy.py 10
nsys stats cupy_profile_${LSB_JOBID}.nsys-rep > cupy_profile_${LSB_JOBID}_stats.txt