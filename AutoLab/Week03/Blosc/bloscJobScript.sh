#!/bin/bash
#BSUB -J bloscbench
#BSUB -q hpc
#BSUB -n 1
#BSUB -W 00:30
#BSUB -R "rusage[mem=8192]"
#BSUB -o /zhome/aa/6/205647/hpc-project/batch_outputs/bloscbench_%J.out
#BSUB -e /zhome/aa/6/205647/hpc-project/batch_errors/bloscbench_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python blosc_program.py 256
python blosc_program.py 512
python blosc_program.py 1024