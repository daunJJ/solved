# 자연수 N 과 젇수 K 입력받기
n, k = map(int, input().split())

# 계산용
result = 1

# 이항 계수 계산하기 
for i in range(k):
  result = result * n  # 분자 곱하기
  result = result / (i+1)  # 분모 나누기
  n = n - 1

print(int(result))