## 1. 환경 설정 
### Conda Environment
```tcsh
# 가상환경 생성
conda env create -f environment.yml -n [environment name]
# 가상환경 활성화
conda activate test

### Module load
```tcsh
# Pyverilog에 필요
module load module load iverilog/12.0
module load license/license
