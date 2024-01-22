# N! 받기 
n = int(input())

# N! 계산하기
import math
facto = math.factorial(n)

# 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수 세기
cnt = 0
for i in range(len(str(facto))-1, 0, -1):
  if (str(facto)[i] == '0' ):
    cnt += 1
  else: 
    break

print(cnt)