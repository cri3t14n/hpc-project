#!/bin/bash
#BSUB -J wallheat_cuda
#BSUB -q c02613
#BSUB -n 4
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=4GB]"
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -W 00:30
#BSUB -o /zhome/aa/6/205647/hpc-project/Mini-Project/outputs/cuda_%J.out
#BSUB -e /zhome/aa/6/205647/hpc-project/Mini-Project/errors/cuda_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

/usr/bin/time -p python simulate_cuda.py 10