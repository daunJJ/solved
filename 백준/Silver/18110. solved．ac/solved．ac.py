### 문제의 난이도 구하기 : 절사 평균 기준 
import sys

## 난이도 의견의 개수 n 받기
n = int(sys.stdin.readline())

## n개의 의견 받기
level = []
for i in range(n):
  level.append(int(sys.stdin.readline()))

## 30% 절사평균 구하기 = 위 15% 아래 15%를 제외한 난이도의 평균 
if n != 0:  # 의견이 하나 이상 있을 때
  # 제외할 의견의 개수
  if (n*15/100 - int(n*15/100)) >= 0.5:  # 반올림
    ignore = int(n*15/100) + 1
  else:
    ignore = int(n*15/100)
  # 제외 후 남는 의견 
  if ignore != 0:  
    rest = sorted(level)[ignore:-ignore]
  else:  # 0개를 제외하는 경우 인덱싱 불가
    rest = sorted(level)
  # 제외 후 남는 의견의 평균 
  if (sum(rest)/len(rest) - int(sum(rest)/len(rest))) >= 0.5:  # 반올림
    print(int(sum(rest)/len(rest)) + 1)
  else:
    print(int(sum(rest)/len(rest)))  
else:  # 의견이 하나도 없을 때
  print(0)