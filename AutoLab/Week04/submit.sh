#!/bin/bash
#BSUB -J hav_lineprof
#BSUB -q hpc
#BSUB -n 1
#BSUB -W 00:20
#BSUB -R "rusage[mem=4096]"
#BSUB -R "select[model == XeonGold6126]"
#BSUB -o /zhome/aa/6/205647/hpc-project/batch_outputs/hav_lineprof_%J.out
#BSUB -e /zhome/aa/6/205647/hpc-project/batch_errors/hav_lineprof_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

kernprof -l haversine.py /dtu/projects/02613_2025/data/locations/locations_100.csv
python -m line_profiler -rmt haversine.py.lprof