# 비교당할 N개의 숫자 받기
import sys
N = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))

# 비교할 M개의 숫자 받기
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

# A 안에 B가 존재하는지 비교
for i in range(M):
  if B[i] in A:
    print(1)
  else:
    print(0)