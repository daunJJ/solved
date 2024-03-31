## 요세푸스 문제 : (N,K)가 주어졌을 때, 원을 따라 N명의 사람 중 K번째 사람을 계속해서 제거 

## N(인원수)과 K(간격) 입력 받기
N, K = map(int, input().split())

## 제거되는 순번 리스트 
eliminate = []

## 순번의 제거 여부를 나타내는 리스트
ox = [0 for i in range(N)]

## 제거되는 순서 출력하기 
j = 0  # j는 (현재 가리키고 있는) 지시 인덱스
while len(eliminate) != N:  # 모두 제거될 때까지
  cnt = 0  # 남아있는 순번을 세는 역할
  while True:
    if ox[j] == 0:  # j번째 순번이 아직 제거되지 않았으면 -> cnt = cnt + 1
      cnt = cnt + 1
    if cnt == K:  # cnt가 K간격에 딱 맞아지면 -> j 순회를 멈춤 
      break
    j = j + 1 # j 순회
    if j > N-1:  # j가 전체 순번 길이(N)을 넘어서면 -> 처음으로 되돌림 
      j = 0  
  # cnt = K 가 되었을 때
  ox[j] = 1  # j번째 순번 제거 여부 : 1
  eliminate.append(j+1)  # 제거된 j번째 순번을 리스트에 추가


## 출력하기
print('<', end='')
for i in range(N-1):
  print(eliminate[i], end=', ')
print(eliminate[N-1], end='')
print('>')