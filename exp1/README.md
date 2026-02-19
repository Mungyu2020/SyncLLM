## 1. 실험 설명
* **1.dataset_for_diffusion:**
    * HDLBITS_solutions로 추출한 RTL을 Sync-LLM의 EDGE Diffusion model 학습 데이터셋 형식에 맞게 SOG Graph를 만들고 graphml형식으로 저장
    * 해당 실험은 GPU-5 서버에서 진행했지만 GPU를 사용하지는 않음
* **2.generated_dataset:**
    * 2-1.저장된 graphml 파일을 이미지로 출력하여 그래프 시각화 (코드 직접 작성)
    * 2-2.MasterRTL처럼 SOG를 내부 SOG 형태(DG.py)로 저장한 뒤에 바로 이미지로 저장하고 시각화(MasterRTL show_graph)
    * 2-1과 2-2가 동일한 그래프이어야지 1.dataset_for_diffusion에서 저장한 graphml 파일이 실제 MasterRTL이 생성한 SOG와 같은지 보장됨
    * 해당 실험은 GPU-5 서버에서 진행했지만 GPU를 사용하지는 않음

## 2. 환경 설정
### Conda Environment
해당 가상환경에서는 Pyverilog, Yosys, MasterRTL은 돌아가지만 SyncircuitData는 돌릴 수 없다. (Yosys 빌드를 위해 python 버전을 3.8 정도로 낮춰 놓음)
AST나 SOG 관련 작업을 할 떄 해당 가상환경을 사용하면 될 것으로 보인다. (Sync-LLM 재현에서는 EDGE diffusion model dataset 생성 정도에 쓰일 듯)

```tcsh
# 가상환경 생성
conda env create -f environment.yml -n [environment name] -y

# 가상환경 활성화
conda activate [environment name]
```

---

## 3. Yosys 빌드 및 설치 (tcsh)
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


### 4. Module Load (yosys 빌드 이후에 진행)
```tcsh
# Pyverilog 실행에 필요한 모듈 로드
module load iverilog/12.0
module load license/license
```
