#!/bin/tcsh
if ( $#argv == 0 ) then
    set env_name = "EDGE"
else
    set env_name = $1
endif

echo "Creating Conda environment: $env_name"
conda create -n $env_name python=3.9 -y
echo "Activating environment..."
conda activate $env_name

setenv PYTHONNOUSERSITE 1
unsetenv PYTHONPATH
conda env config vars set PYTHONNOUSERSITE=1 PYTHONPATH=""

rehash

echo "Installing PyTorch & PyG (Conda based for GLIBC safety)..."
conda install pytorch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 pytorch-cuda=12.1 -c pytorch -c nvidia -y
conda install pyg -c pyg -y
conda install pytorch-scatter pytorch-sparse pytorch-cluster pytorch-spline-conv -c pyg -y

echo "Installing DGL (Pip based with CUDA 12.1)..."
python -m pip install dgl==2.4.0+cu121 -f https://data.dgl.ai/wheels/torch-2.4/cu121/repo.html

echo "Installing Dependencies..."
python -m pip install torchdata==0.8.0 numpy==1.26.4 scipy==1.13.1 networkx==3.2.1 matplotlib==3.9.0
python -m pip install tqdm==4.66.4 prettytable==3.16.0 scikit-learn==1.6.1
python -m pip install tensorboard==2.17.0 wandb==0.24.0 psutil==7.2.1 pandas ipython powerlaw pyemd eden-kernel

echo "Environment $env_name setup complete!"
conda activate $env_name