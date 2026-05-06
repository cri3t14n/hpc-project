#!/bin/bash
#BSUB -J numpy_mt
#BSUB -q hpc
#BSUB -n 8
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model == XeonGold6126]"
#BSUB -W 01:00
#BSUB -o /work3/02613/dump/numpy_mt_%J.out
#BSUB -e /work3/02613/dump/numpy_mt_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

export MPI_NUM_THREADS=8
export OMP_NUM_THREADS=8
export OPENBLAS_NUM_THREADS=8
export MKL_NUM_THREADS=8
export VECLIB_MAXIMUM_THREADS=8
export NUMEXPR_NUM_THREADS=8

python -u matmuls.py