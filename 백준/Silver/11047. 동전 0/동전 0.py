# 동전의 종류 N개와 가치의 합 K 받기
N, K = map(int, input().split())

# N개의 동전 가치 받기 
coin = []
for i in range(N):
  c = int(input())
  coin.append(c)

# K원을 만드는데 필요한 동전 개수의 최소값 구하기
sum = 0  # 필요한 동전 수의 합  

for j in range(len(coin)):  
  sum += K //coin[len(coin)-1-j]  # 맨 마지막 인덱스부터 가능한 동전 수 계산 
  K = K % coin[len(coin)-1-j]  # K원을 만드는데 남은 가격

print(sum)