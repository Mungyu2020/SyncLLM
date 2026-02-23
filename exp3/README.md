# 실험 보고서: RTL 합성 및 추상화 레벨 변환 연구

본 실험은 **Yosys**를 활용하여 원본 RTL을 다양한 형태의 중간 언어(BLIF-RTL, BLIF-Netlist 등)로 변환하고, 이를 **Pyverilog**를 통해 **SOG(Graph)** 형식으로 변환하는 과정에서의 특이사항을 분석

## 1. 용어 정의

| 용어 | 정의 및 설명 |
| :--- | :--- |
| **RTL** | 합성 전, 인간이 읽을 수 있는 수준의 원본 Verilog 코드 |
| **BLIF-RTL** | Yosys 합성을 통해 생성된 단순화된 문법의 RTL |
| **BLIF-Netlist** | Tech-mapping 직전 단계의 Netlist (BLIF-RTL과 같은? 유사한? 추상화 레벨) |
| **SOG** | BLIF-RTL을 Pyverilog AST로 변환 후 파싱하여 생성한 새로운 그래프 형식 (MasterRTL 자료구조) |

> **[참고]** 실험 결과, BLIF-RTL과 BLIF-Netlist는 Yosys 내부 DB를 공유하며 `write_verilog` 시 `-noexpr` 옵션 유무에 따라 출력 포맷만 달라지는 것으로 판단

---

## 2. 실험 환경
* **Server:** GPU-5 Server
* **Tool:** Yosys, Pyverilog

---

## 3. 실험 상세 (Execution)

### 실험 1: 기본 RTL 변환
* **목적:** 원본 RTL을 BLIF-RTL로 변환
* **내용:** masterRTL과 동일한 방식은 아니나, RTL을 간단한 문법의 BLIF-RTL로 변환함
* **실행 명령어:**
  ```tcsh
    yosys yosys_script/1_RTL_to_BLIF_RTL.ys

### 실험 1.5: 1-bit 분리 기반 RTL 변환 
* **목적:** SOG 생성을 위해 BLIF-RTL 파싱 단계에서 발생하는 Pointer 및 Concatenation 문법 관련 오류 해결 
* **내용:** 실험 1과 동일하나, 생성된 BLIF-RTL의 모든 assign문을 1-bit 단위로 분리 (splitnets -ports 옵션 추가) 
* **실행 명령어:**
  ```tcsh
    yosys yosys_script/1.5_RTL_to_BLIF_RTL.ys

### 실험 2: BLIF 기반 Netlist 생성 
* **목적:** 원본 RTL을 BLIF-Netlist로 변환 
* **특이사항:** 변환 후에도 일부 assign문이 남아있는 현상 발생 (원인 분석 필요) 
* **실행 명령어:**
  ```tcsh
    yosys yosys_script/2_RTL_to_BLIF_Netlist.ys

### 실험 2.5: 정제된 Netlist 생성 
* **목적:** 실험 1.5의 로직을 적용한 고도화된 BLIF-Netlist 생성 
* **내용:** 실험 1.5의 BLIF-RTL을 기반으로 Netlist 생성 시 assign문이 완전히 사라짐을 확인 
* **실행 명령어:**
  ```tcsh
    yosys yosys_script/2.5_RTL_to_BLIF_Netlist.ys

### 나머지 실험 3, 3.5, 4, 4.5는 실험 이름만 보면 유추할 수 있다.
---

## 4. 환경 설정
SyncLLM/exp1 환경과 동일