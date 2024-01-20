# 보드의 크기 입력 받기 
n, m = map(int, input().split())

#  보드 색상 입력 받기
row = [input() for _ in range(n)]

# 체스 보드를 미리 입력 해둠 
chess1 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
chess2 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']

# 최소값 
min = 100

for x in range(n-7):  # 가로줄 가능한 8개씩
  for y in range(m-7):  # 세로줄 가능한 8개씩
    num1 = 0  # chess1과 비교하여 바꾸어야 할 색 갯수
    num2 = 0  # chess2와 비교하여 바꾸어야 할 색 갯수
    for i in range(8):
      for j in range(8):
        if (row[i+x][j+y] != chess1[i][j]) : num1 = num1 + 1  # chess1판과 비교
        elif (row[i+x][j+y] != chess2[i][j]): num2 = num2 + 1  # chess2판과 비교
    # 최소값 저장
    if (num1 >= num2) : 
      if (min > num2) :
        min = num2
    elif (min > num1) :
      min = num1

print(min)