#!/bin/bash
#BSUB -J sleep_4cores
#BSUB -q hpc
#BSUB -n 4
#BSUB -R "span[hosts=1]"
#BSUB -W 00:02
#BSUB -o sleep_4cores_%J.out
#BSUB -e sleep_4cores_%J.err

/bin/sleep 60