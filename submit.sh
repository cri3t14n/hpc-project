#!/bin/bash
#BSUB -J simulate_time

#BSUB -q hpc

#BSUB -W 20
# Time limit in minutes

#BSUB -R "rusage[mem=2GB]"
# Memory request

#BSUB -n 1
# Number of CPU cores

#BSUB -R "span[hosts=1]"
# Keep resources on one node

#BSUB -o simulate_time_%J.out
#BSUB -e simulate_time_%J.err

#BSUB -u cristianplacinta04@gmail.com
#BSUB -B
#BSUB -N

# source ~/.bashrc
# source .venv/bin/activate

kernprof -l simulate.py