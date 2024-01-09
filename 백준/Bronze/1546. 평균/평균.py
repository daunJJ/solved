# 시험 본 과목 개수 받기
N = int(input())

# 실제 시험 성적 받기
score = list(map(int, input().split()))

# 최대값
max = sorted(score)[N-1]

# 조작된 점수의 평균 구하기
sum = 0 
for i in range(N):
  sum = sum + score[i]/max*100

print(sum/N)