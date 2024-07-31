#!/bin/bash
##x -p gpu
#SBATCH -p cpu
##x --gpus=1
#SBATCH --mem=16gb
#SBATCH -J train
#SBATCH --output=job_metrics.out

export LD_LIBRARY_PATH="/lnet/aic/opt/cuda/cuda-10.2/lib64:/lnet/aic/opt/cuda/cuda-10.2/cudnn/8.0.5/lib64"

.venv/bin/python3 -u -m model
