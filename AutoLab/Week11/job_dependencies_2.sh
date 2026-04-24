#!/bin/bash
#BSUB -J waitall
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -w "ended(21241475)"
#BSUB -o waitall_%J.out
#BSUB -e waitall_%J.err

/bin/sleep 10