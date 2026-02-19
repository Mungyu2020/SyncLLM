# Sync-LLM: RTL to SOG Graph Preprocessing Pipeline

HDLBITS_solutions에서 얻은 RTL을 Sync-LLM 모델(Edge Diffusion)의 입력 형태인 SOG 기반 GraphML 데이터로 변환하는 코드입니다.

## Prerequisites

* **OS:** RHEL 9.4 (Plow) - GPU5,GPU8
* **Shell:** `tcsh` 
* **Python:** 3.9+ 
* **EDA Tools:**
  * **Yosys:** RTL 합성 및 SOG Netlist 생성용
  * **Icarus Verilog:** Pyverilog 파싱 엔진용

---

## How to Use

데이터 변환은 총 3단계 스크립트로 진행. 모든 경로는 프로젝트 루트 디렉토리(exp1_~) 기준.

### Step 1. RTL 파일명 정규화 (`1.rename_RTL.py`)
HDLBits 솔루션에서 파싱한 원본 RTL 파일들의 이름을 이후 단계의 **Top Module 이름**으로 사용하기 위해 파일명을 수정.

* **입력:** `Data/1.RTL_raw/*.v`
* **출력:** `Data/2.RTL/*.v`
* **주요 기능:**
  * 파일명 내 특수문자를 제거하고 언더바(`_`)로 치환.
  * 숫자로 시작하는 파일명 앞에 `_`를 추가하여 Verilog 식별자 규칙을 준수.
* **실행:**
  ```tcsh
  python 1.rename_RTL.py

### Step 2. Top Module 이름 일괄 수정 (`2.rename_topmodule_name.py`)
RTL 코드 내부의 모듈 선언부(module top_module ...)를 실제 파일명과 일치하도록 수정

* **입력:** `Data/2.RTL/*.v`
* **출력:** `Data/3.RTL_final/*.v`
* **주요 기능:**
  * Pyverilog AST 파서를 활용하여 코드 내 모듈 이름을 파일명 기반으로 자동 치환. 
  * 파싱 에러 발생 시 해당 파일을 건너뛰고 마지막에 Faulty Files List를 출력
* **실행:**
  ```tcsh
  python 2.rename_topmodule_name.py

### Step 3. RTL to SOG & GraphML 변환 (`3.rtl_to_sog.py`)
MasterRTL 코드를 활용하여 정제된 RTL을 SOG 구조의 넷리스트로 합성하고, 이를 최종 GraphML 포맷으로 변환

* **입력:** `Data/3.RTL_final/*.v`
* **출력:** `SOG Verilog: Data/4.SOG/*_sog.v`, `GraphML 데이터: Data/4.Output_graphml/*.graphml`
* **주요 기능:**
  * Yosys Synthesis: yosys script를 통해 합성을 진행하고 SOG graph(./vlg2ir/DG.py)로 변환.
  * Graph Extraction: ./vlg2ir/analyze.py를 호출하여 넷리스트를 GraphML 형태의 SOG 그래프로 추출. 
* **실행:**
  ```tcsh
  python 3.rtl_to_sog.py


## Notes (참고사항)

* **MasterRTL 사전 설정**: `3.rtl_to_sog.py`를 실행하기 전, `MasterRTL/vlg2ir/analyze.py` 코드 내에 `graph2graphml()` 함수가 구현되어 있어야 정상적으로 `.graphml` 파일이 생성.
* **SOG 활용**: 생성된 `graphml` 형태의 SOG 그래프는 향후 **Sync-LLM의 EDGE diffusion model** 학습 및 활용에 사용될 예정.
* **Error Handling & Faulty Files**:
    * 파싱 단계(`2.rename_topmodule_name.py`)에서 에러가 발생한 디자인은 스킵되며, 마지막에 요약된 `Faulty Files List`를 통해 실패 원인을 확인할 수 있음.
    * 합성 단계(`3.rtl_to_sog.py`)에서 실패한 디자인은 `fault_design` 리스트에 저장되어 마지막에 출력.
* **Environment**: 가상환경 활성화 상태에서 `yosys` 및 `iverilog`의 실행 경로(`PATH`)가 올바르게 설정되어 있는지 확인 필요.