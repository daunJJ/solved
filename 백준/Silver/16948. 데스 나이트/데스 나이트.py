from collections import deque

# 체스판의 크기 
N = int(input())

# (r1, c1) -> (r2, c2) 받기
r1, c1, r2, c2 = map(int, input().split())
start = (r1, c1)
goal = (r2, c2)

# BFS로 최소 이동 횟수 구하기 
def BFS(start, goal, N):
  # 초기화
  pre = (*start, 0)  # (r1, c1, 시간)  = 시작 노드 
  queue =  deque([pre])  # 방문할 노드 
  visited = set([start])  # 방문한 노드

  # 너비 우선 탐색 수행 
  while queue:
    r, c, time = queue.popleft()
    visited.add((r,c))  # (r, c) 위치만 저장 

    if (r,c) == goal: # 성공 조건 
      return time  # 이동 횟수 리턴 
    
    # 이동 가능한 방향 
    for move_r, move_c in ((r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)):
      if (0 <= move_r < N) & (0 <= move_c < N) & ((move_r, move_c) not in visited):  # 체스판 벗어나지 않음 + 방문 안 함 
        visited.add((move_r, move_c))  # 이동 가능 => 방문 처리 
        queue.append((move_r, move_c, time+1))
  
  # 탐색 실패 
  return -1

print(BFS(start, goal, N))