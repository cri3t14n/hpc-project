#!/bin/bash
#BSUB -J cpu_type_sleep
#BSUB -q hpc
#BSUB -W 00:02
#BSUB -R "select[model == XeonGold6126]"
#BSUB -o cpu_type_sleep_%J.out
#BSUB -e cpu_type_sleep_%J.err

echo "CPU model from environment:"
echo "$LSB_HOSTS"
lscpu | grep "Model name"

/bin/sleep 60