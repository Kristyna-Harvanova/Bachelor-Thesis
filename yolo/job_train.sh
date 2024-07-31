#!/bin/bash
##x -p gpu
#SBATCH -p cpu
##x --gpus=1
#SBATCH --mem=16gb
##SBATCH --mem=32gb
#SBATCH -J train
#SBATCH --output=final_job_staffMeasure_without_seep_eval.out 

export LD_LIBRARY_PATH="/lnet/aic/opt/cuda/cuda-10.2/lib64:/lnet/aic/opt/cuda/cuda-10.2/cudnn/8.0.5/lib64"

.venv/bin/python3 -u -m model
