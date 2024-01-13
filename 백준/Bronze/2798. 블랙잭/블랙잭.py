# N과 M을 입력 받음
n, m = map(int, input().split())

# N장의 숫자를 입력 받음
num = list(map(int, input().split()))

# 3장을 더해 M과 가장 가까운 수 출력
best = 0  # 현재 가장 가까운 수
for i in range(n-2):
  for j in range(i+1, n-1):
    for k in range(j+1, n):
      sum = 0 # 3장의 합 
      sum = num[i] + num[j] + num[k]
      if (sum <= m) and (((m - sum) < (m - best))) :
          best = sum
print(best)