# N개 입력 받기
import sys
N = int(sys.stdin.readline())

# N개의 숫자 입력 받기
num_list = []
for i in range(N):
  num_list.append(int(sys.stdin.readline()))

# 오름차순 정렬 후 하나씩 출력 
num_list.sort()

for i in range(N):
  print(num_list[i])