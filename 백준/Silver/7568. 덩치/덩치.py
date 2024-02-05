# 전체 사람의 수 받기
N = int(input())

# (몸무게, 키) 받기 -> 리스트 내 리스트 형태
wh = [ list(map(int, input().split())) for _ in range(N) ]

# 등수 계산 
for i in wh:  # 앞에서부터 한 명 씩
  num = 1
  for j in wh: # 모든 사람들과 비교
    if (i[0] < j[0]) & (i[1] < j[1]):  # 몸무게와 키가 다른 사람보다 작을 때마다 num + 1
      num = num + 1
  print(num, end=' ')  # 줄바꿈 없이 출력