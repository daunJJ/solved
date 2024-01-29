# N 개의 숫자 받기
import sys
N = int(sys.stdin.readline())

# 숫자를 입력받는 list
numList = []
# 빈도수를 저장하는 dict
numDict = {}

# 숫자와 빈도수 입력 받기
for i in range(N):
  number = int(sys.stdin.readline()) 
  # 리스트에 숫자 추가
  numList.append(number)
  # 빈도수 저장 
  if number in numDict:
    numDict[number] += 1
  else:
    numDict[number] = 1

# 산술 평균 계산 
print(int(round(sum(numList)/N, 0)))

# 중앙값 계산 
print(sorted(numList)[int(N/2)])

# 최빈값 계산 
# 빈도수가 가장 큰 값들만 저장
maxDict = max(numDict.values())  # 가장 큰 빈도수
mode = [k for k, value in numDict.items() if maxDict == value ]  # 가장 큰 빈도수의 number

# 최빈값 출력하기
if len(mode) > 1:  # 최빈값이 2개 이상이면
  print(sorted(mode)[1])
else:  # 최빈값이 1개이면
  print(sorted(mode)[0])

# 범위 계산 
print(max(numList) - min(numList))