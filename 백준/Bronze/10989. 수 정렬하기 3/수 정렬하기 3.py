# 시간 초과 문제
import sys
# input = sys.stdin.readline

# 개수 N 받기
N = int(sys.stdin.readline())

# 최대 입력 개수의 리스트
num = [0] * 10001

# 입력 값의 해당하는 리스트 인덱스의 값 증가
for i in range(N):
  num[int(sys.stdin.readline())] += 1

# 작은 값부터 출력
for i in range(len(num)):
  if num[i] != 0:
    # 갯수만큼
    for j in range(num[i]):
      print(i)