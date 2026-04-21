#!/bin/bash
#BSUB -J notify_sleep
#BSUB -q hpc
#BSUB -W 00:02
#BSUB -B
#BSUB -N
#BSUB -o notify_sleep_%J.out
#BSUB -e notify_sleep_%J.err

/bin/sleep 60