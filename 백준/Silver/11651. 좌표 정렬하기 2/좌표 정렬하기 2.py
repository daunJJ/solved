# 2차원 평면위의 점의 갯수 N 받기
N = int(input())

# N개의 좌표를 받을 리스트 마련
grid = []

# N개의 좌표 받기
for i in range(N):
  x, y = map(int, input().split())
  grid.append([x,y])

# y좌표가 증가하는 순 > x좌표가 증가하는 순서대로 정렬 후 출력
# y좌표 > x좌표 증가하는 순으로 정렬
grid.sort(key=lambda point: (point[1], point[0]))

# 출력하기
for j in range(N):
  print(grid[j][0], grid[j][1])