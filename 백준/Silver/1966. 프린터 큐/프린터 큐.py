# 테스트 케이스의 수 받기
test = int(input())

# 큐 모듈 호출
from collections import deque

# 문서 수, 궁금한 문서의 위치, 문서들의 중요도 받기
for i in range(test):
  n, m = map(int, input().split())
  importance = list(map(int, input().split()))
  # 인덱스 리스트
  pos = [i for i in range(n)]
  # 출력 순서 저장
  cnt = 0
  # 출력 함수
  while m in pos: # 궁금한 문서의 인덱스가 인덱스 리스트에 남아있는 동안
    while max(importance) != importance[0]:  # 맨 앞 중요도가 max를 만나면 중지
      importance.append(importance.pop(0))  # 맨 앞 중요도를 맨 뒤로 이동
      pos.append(pos.pop(0))  # 맨 앞 인덱스를 맨 뒤로 이동 
    importance.pop(0)  # max를 만나 pop 
    pos.pop(0)  
    cnt = cnt + 1
  print(cnt)