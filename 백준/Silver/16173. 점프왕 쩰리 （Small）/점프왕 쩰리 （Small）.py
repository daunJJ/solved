# 게임 구역의 크기
N = int(input())

# 게임판 받기
gamepan = []
for i in range(N):
  line = list(map(int, input().split()))
  gamepan.extend(line)

# 이동 가능 여부 
right = [0 for i in range(N*N)]
below = [0 for i in range(N*N)]

# 초기화 
move = [0]
i = 0

# move로 깊이 우선 탐색을 하면서 위치 저장
while True: 
  if gamepan[i] == -1:  # 성공 종료 조건 
    print_str = 'HaruHaru'
    break
  if (right[0] == 1) & (below[0] == 1):  # 실패 종료 조건
    print_str = 'Hing'
    break
  if gamepan[i] == 0:  # 실패 종료 조건
    print_str = 'Hing'
    break
  if right[i] == 0:  # 오른쪽 이동 시도 
    next = i + gamepan[i]
    if i%N + gamepan[i] >= N:  # 게임판을 벗어남
      right[i] = 1  # 오른쪽 이동 불가능
    else: 
      i = next  # 오른쪽 이동
      move.append(i)
    continue 
  if below[i] == 0:  # 아래쪽 이동 시도
    next = i + gamepan[i] * N
    if i//N + gamepan[i] >= N:  # 게임판을 벗어남
      below[i] = 1  # 아래쪽 이동 불가능 
    else:
      i = next  # 아래쪽 이동 
      move.append(i)
    continue 
  if (right[i] == 1) & (below[i] == 1):  # 이동 불가 
    if i - move[-2] < N:  # 직전에 오른쪽으로 이동하였음
      move.pop()  # 현 위치 POP
      i = move[-1]  # 직전 위치로 돌아감 
      right[i] = 1
    elif i - move[-2] >= N:  # 직전에 아래로 이동하였음
      move.pop()  # 현 위치 POP 
      i = move[-1]  # 직전 위치로 돌아감 
      below[i] = 1 
  
print(print_str)