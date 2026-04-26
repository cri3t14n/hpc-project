#!/bin/bash
#BSUB -J wallheat_ref
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=4096]"
#BSUB -W 04:00
#BSUB -o /zhome/aa/6/205647/hpc-project/Mini-Project/outputs/wallheat_ref_%J.out
#BSUB -e /zhome/aa/6/205647/hpc-project/Mini-Project/errors/wallheat_ref_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026


# echo "Timing reference simulate.py for N=10"
/usr/bin/time -p python ../simulate.py 10