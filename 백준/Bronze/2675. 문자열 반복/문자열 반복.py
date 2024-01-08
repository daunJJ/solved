# 테스트 케이스 갯수 받기
test = int(input())

# 테스트 케이스 갯수 만큼의 행으로 구성된 2차원 리스트
l= [input().split() for _ in range(test)]

# 반복 출력
for i in range(test):
  for j in range(len(l[i][1])):
    if j < (len(l[i][1])-1):
      print(l[i][1][j] * int(l[i][0]), end="")  # for문을 반복하며 줄바꿈이 되지 않도록
    else:
      print(l[i][1][j] * int(l[i][0]))