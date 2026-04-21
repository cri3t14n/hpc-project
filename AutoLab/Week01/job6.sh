#!/bin/bash
#BSUB -J sleep_64cores
#BSUB -q hpc
#BSUB -n 64
#BSUB -R "span[hosts=1]"
#BSUB -W 00:02
#BSUB -o sleep_64cores_%J.out
#BSUB -e sleep_64cores_%J.err

/bin/sleep 60