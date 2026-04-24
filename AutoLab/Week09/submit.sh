#!/bin/sh
#BSUB -q c02613
#BSUB -J cuda_add
#BSUB -n 4
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=1GB]"
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -W 00:30
#BSUB -o cuda_add_%J.out
#BSUB -e cuda_add_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

python vector_addition.py