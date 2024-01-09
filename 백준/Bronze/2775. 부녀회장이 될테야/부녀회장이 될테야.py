# test case 개수 받기
test = int(input())

# 케이스 입력 받고 계산
for i in range(test):
  k = int(input())
  n = int(input())
  floor = [x for x in range(1, n+1)]  # 0층 기본값
  for i in range(k):
    for j in range(1, n):
      floor[j] = floor[j] + floor[j-1] 
  print(floor[-1])  # 가장 마지막 원소 출력