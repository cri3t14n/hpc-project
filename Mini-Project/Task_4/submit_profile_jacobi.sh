#!/bin/bash
#BSUB -J wallheat_prof
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=4096]"
#BSUB -W 04:00
#BSUB -o /zhome/aa/6/205647/hpc-project/Mini-Project/outputs/wallheat_prof_%J.out
#BSUB -e /zhome/aa/6/205647/hpc-project/Mini-Project/errors/wallheat_prof_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

python -m kernprof -l -o simulate_${LSB_JOBID}.py.lprof ../simulate.py 10
python -m line_profiler simulate_${LSB_JOBID}.py.lprof > simulate_${LSB_JOBID}_profile.txt