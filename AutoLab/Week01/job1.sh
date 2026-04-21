#!/bin/bash
#BSUB -J simple_sleep
#BSUB -q hpc
#BSUB -W 00:02
#BSUB -o simple_sleep_%J.out
#BSUB -e simple_sleep_%J.err

/bin/sleep 60