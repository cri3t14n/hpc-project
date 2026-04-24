#!/bin/bash
#BSUB -J myarray[2,29,71,73,127]
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -o myarray_%J_%I.out
#BSUB -e myarray_%J_%I.err

/bin/sleep 10