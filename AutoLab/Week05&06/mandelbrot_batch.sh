#!/bin/bash
#BSUB -J mandelbrot_speedup
#BSUB -q hpc
#BSUB -n 16
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=4096]"
#BSUB -R "select[model == XeonGold6126]"
#BSUB -W 00:30
#BSUB -o /zhome/aa/6/205647/hpc-project/batch_outputs/mandelbrot_speedup_%J.out
#BSUB -e /zhome/aa/6/205647/hpc-project/batch_errors/mandelbrot_speedup_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

for p in 1 2 4 8 16
do
    echo "num_proc=$p"
    /usr/bin/time -p python mandelbrot.py $p
done