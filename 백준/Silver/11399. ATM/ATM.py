# ATM기에 줄을 선 사람의 수 N명 받기 
N = int(input())

# N명의 사람이 돈을 인출하는데 걸리는 시간 받기
time = list(map(int, input().split()))

# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최소값 구하기
# 풀이: 앞 사람의 시간은 누적되어 합해지므로 걸리는 시간이 적은 사람부터 인출하는게 가장 효율적임 
# 1. 걸리는 시간이 적은 순으로 정렬
time = sorted(time)
# 2. 누적 합 계산
total_time = 0
for i in range(N):
  total_time += sum(time[:i+1])

print(total_time)