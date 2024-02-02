# 카드의 개수 N 받기
N = int(input())

# 큐로 구현하기 (FIFO)
from collections import deque

# N까지의 숫자로 구성된 리스트 생성
card = deque()
for i in range(1, N+1):
  card.append(i)

while len(card) > 1:  # card가 1개 남을 때 까지
  card.popleft()  # 맨 앞 카드를 버리기
  card.append(card.popleft())  # 그 다음 카드를 맨 뒤로 옮기기

print(card[0])  # 마지막까지 남은 카드 출력