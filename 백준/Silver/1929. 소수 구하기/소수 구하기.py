# 에라토스테네스의 체
# m ~ n 받기
m, n = map(int, input().split())

# 0부터 소수이면 True, 아니면 False
a = [False,False] + [True]*n
# 소수를 저장할 리스트
primes=[]

for i in range(2, n+1):
  if a[i]:  # 소수이면 
    primes.append(i)  # prime 리스트에 저장 
    if i >= m:
      print(i)
    for j in range(2*i, n+1, i): # 소수의 배수들은 False로 바꿈
        a[j] = False