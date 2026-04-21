#!/bin/bash
#BSUB -J parallel_pi
#BSUB -q hpc
#BSUB -n 10
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=2048]"
#BSUB -R "select[model == XeonGold6126]"
#BSUB -W 00:20
#BSUB -o /zhome/aa/6/205647/hpc-project/batch_outputs/parallel_pi_%J.out
#BSUB -e /zhome/aa/6/205647/hpc-project/batch_errors/parallel_pi_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

echo "===== SERIAL ====="
/usr/bin/time -p python pi_serial.py

echo "===== FULLY PARALLEL ====="
/usr/bin/time -p python pi_parallel.py

echo "===== CHUNKED PARALLEL ====="
/usr/bin/time -p python pi_chunked.py