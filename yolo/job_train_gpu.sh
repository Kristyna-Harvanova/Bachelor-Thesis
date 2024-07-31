#!/bin/bash
#SBATCH -p gpu      
#SBATCH -G 1       
#SBATCH -t 2000                  
#SBATCH --mem 32G
#SBATCH -J gpu_train                     
#SBATCH --output=final_job_staff_augm_all_eval.out                 

# export LD_LIBRARY_PATH="/lnet/aic/opt/cuda/cuda-10.2/lib64:/lnet/aic/opt/cuda/cuda-10.2/cudnn/8.0.5/lib64"
export LD_LIBRARY_PATH="/lnet/aic/opt/cuda/cuda-11.2/lib64:/lnet/aic/opt/cuda/cuda-11.2/cudnn/8.1/lib64"

.venv/bin/python3 -u -m model


