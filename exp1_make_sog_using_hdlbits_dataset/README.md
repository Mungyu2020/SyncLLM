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

## 2. Yosys 빌드 및 설치 (tcsh)

가상환경이 활성화된 상태에서 아래 명령어를 순서대로 입력하여 Yosys를 빌드하고 설치.

```tcsh
# yosys 폴더로 이동
cd ../yosys
# GCC 기반 빌드 설정 생성
make config-gcc
make -j`nproc`
# 가상환경($CONDA_PREFIX) 경로에 설치
make install PREFIX=$CONDA_PREFIX