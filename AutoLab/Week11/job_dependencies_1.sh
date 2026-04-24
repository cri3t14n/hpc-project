#!/bin/bash
#BSUB -J waitjob
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -w "done(1234567)"
#BSUB -o waitjob_%J.out
#BSUB -e waitjob_%J.err

/bin/sleep 10