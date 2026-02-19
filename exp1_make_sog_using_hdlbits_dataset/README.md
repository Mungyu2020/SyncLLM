## 1. 환경 설정
### Conda Environment
```tcsh
# 가상환경 생성
conda env create -f environment.yml -n [environment name] -y

# 가상환경 활성화
conda activate [environment name]
```

---

## 2. Yosys 빌드 및 설치 (tcsh)
가상환경이 활성화된 상태에서 아래 명령어를 순서대로 입력하여 Yosys를 빌드하고 설치.

```tcsh
# yosys 폴더로 이동
cd yosys

# GCC 기반 빌드 설정 생성
make config-gcc

# 병렬 컴파일 실행 (tcsh 문법: 백틱 사용)
make -j`nproc`

# 가상환경($CONDA_PREFIX) 경로에 설치
make install PREFIX=$CONDA_PREFIX

# 환경 변수 설정 (PATH 및 라이브러리 경로): module load 전에 해야 함
setenv PATH ${CONDA_PREFIX}/bin:$PATH
setenv LD_LIBRARY_PATH ${CONDA_PREFIX}/lib:$LD_LIBRARY_PATH

# 명령어 테이블 갱신
rehash
```


### 3. Module Load (yosys 빌드 이후에 진행)
```tcsh
# Pyverilog 실행에 필요한 모듈 로드
module load iverilog/12.0
module load license/license
```
