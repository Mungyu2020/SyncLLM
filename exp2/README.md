## 1. 실험 설명
* **Note:**
    * exp1에서 추출한 Graphml 형태의 SOG Graph를 활용하여 EDGE diffusion model 학습 작동 여부 체크
    * 여러 레포지토리의 패키지 버전이 혼재되어 있어, 상호 호환성 확인 프로세스 포함
    * **중요:** 해당 실험은 RHEL 8 기반의 **GPU-8 서버**에서 진행 (GLIBC 호환성을 위해 반드시 GPU-8에서 환경 구축 권장)

## 2. 환경 설정
해당 가상환경은 SyncircuitData을 돌리기 위해 존재한다. (exp1과 다른 가상환경임)

Version 1
```tcsh
# 가상환경 생성 (>3 hours)
conda env create -f environment.yml -n [environment name]

# 가상환경 활성화
conda activate [environment name]

# 로컬 패키지 참조 및 외부 경로 차단
conda env config vars set PYTHONNOUSERSITE=1
conda env config vars set PYTHONPATH=""

# 설정 반영을 위한 재활성화
conda activate [environment name]

# 나머지 패키지 설치
python -m pip install -r requirements.txt

rehash
```

Version 2 (Recommended)
 ```tcsh
# 가상환경 생성 (<10 min)
tcsh install_env.csh [environment name]
```

## 3. 코드 수정 사항
1. skeleton_gen/EDGE/eval_utils/evaluation/models/gin/gin.py
    - "r" 이라는 문자가 코드 중간에 삽입돼서 삭제
2. skeleton_gen/EDGE/datasets/data.py
    - g_max_degree = max([d for _, d in g.degree()])에서 ValueError: max() arg is an empty sequence 문제 발생
    - new_g.number_of_nodes() == 0: 이면 continue하도록 수정 (하드코딩, 데이터셋 문제인지 오류인지 점검 필요)
3. skeleton_gen/EDGE/skeleton_designs
    - 학습 데이터셋 부재로 exp1에서 생성한 .graphml 파일 추가
4. skeleton_gen/EDGE/eval_utils/evaluation/graph_structure_evaluation.py
    - mmd = K_GG.mean() + K_RR.mean() - (2 * K_GR.mean())에서 RuntimeWarning: Mean of empty slice.
    - 2번 문제랑 관련 있어보임. 구체적인 이유는 아직 확인 불가