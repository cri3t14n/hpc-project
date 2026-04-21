#!/bin/bash
#BSUB -J sleep_16cores
#BSUB -q hpc
#BSUB -n 16
#BSUB -R "span[hosts=1]"
#BSUB -W 00:02
#BSUB -o sleep_16cores_%J.out
#BSUB -e sleep_16cores_%J.err

/bin/sleep 60