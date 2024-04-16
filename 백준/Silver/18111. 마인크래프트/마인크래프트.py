## 집터 내의 땅의 높이를 일정하기 바꾸기
# N (세로) * M(가로) 크기의 집터
# 집터 맨 왼쪽 위 좌표는 (0,0)

## 할 수 있는 작업
# 1. 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣기 (2초)
# 2. 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓기 (1초)

## 규칙
# 작업을 시작할 때 인벤토리에는 B개의 블록이 들어있음
# 땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없음

## N, M, B 받기
N, M, B = map(int, input().split())

## N개 줄에 걸쳐 M개의 정수로 (i,j)의 땅의 높이 받기
# 2차원 배열로 받기
height = []
for i in range(N):
  height.append(list(map(int, input().split())))

## 땅 고르기
# 1번 작업: 제거하기 (2초)
a = 0
# 2번 작업: 넣기 (1초)
b = 0

# 좌표별 높이 Count {높이:개수}
count = {}
for i in range(N):
  for j in range(M):
    if height[i][j] not in count.keys():
      count[height[i][j]] = 1
    else:
      count[height[i][j]] += 1

# 집터 높이의 최대값과 최소값 받기
min_h = sorted(count.items(), key=lambda x:x[0])[0][0]
max_h = sorted(count.items(), key=lambda x:x[0])[-1][0]

# 시간 변수
time = float("inf") 

# [최대 높이 ~ 최소 높이]까지 높이별로 필요한 블럭 수와 필요 시간 측정 
for h in range(max_h, min_h - 1, -1):
  a = 0
  b = 0
  # 기준 높이를 기준으로 필요한 블럭 개수 세기
  for key in count.keys():
    if key > h:  # 기준 높이보다 높으면
      a += (key - h) * count[key] # 제거할 개수
    elif key < h:  # 기준 높이보다 낮으면
      b += (h - key)  * count[key]  # 넣을 개수
  # time_pre(현재 측정 시간)
  time_pre = a*2 + b*1
  # b(넣어야할 블럭 개수)가 B(인벤토리에 있는 블록 개수) + a(제거된 블럭의 개수)보다 작다면
  if b <= (B+a):
    if time_pre < time:
      time = time_pre
      ground = h

print(time, ground)