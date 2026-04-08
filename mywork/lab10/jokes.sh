#!/bin/bash
#SBATCH --account=ds2002
#SBATCH --partition=standard
#SBATCH --job-name=lolcow_jokes
#SBATCH --output=jokes_%j.out
#SBATCH --error=jokes_%j.err
#SBATCH --time=00:01:00
#SBATCH --mem=8GB
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --array=1-10

module load apptainer
apptainer run ~/lolcow-latest.sif