import glob
import os
import math

files = glob.glob('./Data/4.Output_graphml/*.graphml')

counts = []         
deleted_count = 0  

print("=== 노드 개수 820개 이상 파일 삭제 작업 시작 ===")
for f in files:
    try:
        with open(f, 'r', encoding='utf-8', errors='ignore') as d:
            cnt = d.read().count('<node')
            
            if cnt >= 820:
                print(f"[삭제됨] {os.path.basename(f)} : 노드 {cnt}개")
                os.remove(f)  
                deleted_count += 1
            else:
                counts.append(cnt) 

    except Exception as e:
        print(f"Error processing {f}: {e}")

print(f"=== 작업 완료: 총 {deleted_count}개 파일 삭제됨 ===\n")

avg = sum(counts) / len(counts)
min_val = min(counts)
max_val = max(counts)
counts.sort()
median = counts[len(counts)//2]

print(f'=== [정제 후] GraphML 노드 개수 분석 (총 {len(counts)}개 파일) ===')
print(f'최소: {min_val}')
print(f'최대: {max_val}')
print(f'평균: {avg:.2f}')
print(f'중위: {median}')

print('\n=== 구간별 분포 ===')
if max_val == 0: max_val = 1
bin_size = max(5, math.ceil(max_val / 10)) 
bins = {}

for c in counts:
    b = (c // bin_size) * bin_size
    bins[b] = bins.get(b, 0) + 1

for b in sorted(bins.keys()):
    range_str = f'{b:3d} ~ {b+bin_size-1:3d}'
    bar = '*' * bins[b]
    print(f'{range_str}: {bins[b]:3d}개 | {bar}')