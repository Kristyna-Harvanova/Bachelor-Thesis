#!/bin/bash
##x -p gpu
#SBATCH -p cpu
##x --gpus=1
#SBATCH --mem=4gb
#SBATCH -J augm
#SBATCH --output=job.out

export LD_LIBRARY_PATH="/lnet/aic/opt/cuda/cuda-10.2/lib64:/lnet/aic/opt/cuda/cuda-10.2/cudnn/8.0.5/lib64"

.venv/bin/python3 -u -m app.datasets.training
# .venv/bin/python3 -u -m app.datasets.evaluation
# .venv/bin/python3 -u -m app.datasets.augmentation
# .venv/bin/python3 -u -m app.datasets.augmentation --take 2

