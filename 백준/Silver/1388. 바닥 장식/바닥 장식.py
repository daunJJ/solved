# 세로크기 n, 가로크기 m
n, m = map(int, input().split())

# 지나 갔는지 확인용 행렬
mat = mat = [[0 for i in range(m)] for j in range(n)]

# 판자 입력 받기 
panja = []
for k in range(n):
   panja.append(list(input()))

# 판자의 개수
cnt = 0

# 필요한 판자의 개수 세기 
for sero in range(n):
  for garo in range(m):
    if mat[sero][garo] == 0:  # 아직 거치지 않은 판자이면 
      if panja[sero][garo] == '-':  # - 인지 ㅣ인지 확인 
        mat[sero][garo] = 1  # mat 지나감을 표시 
        move = garo+1  # - 이면 오른쪽으로 이동하여 -가 연결되는지 확인 
        while move < m:  # -가 연결되는 동안 mat 지나감 표시 
          if panja[sero][move] == '-':
            mat[sero][move] = 1
            move += 1
          else:
            break
        cnt += 1
      elif panja[sero][garo] == '|': # ㅣ 일 때 
        mat[sero][garo] = 1
        move = sero+1  # l 이면 아래로 이동하여 l 가 연결되는지 확인 
        while move < n:  # ㅣ 가 연결되는 동안 mat 지나감 표시
          if panja[move][garo] == '|':
            mat[move][garo] = 1
            move += 1
          else:
            break
        cnt += 1
    else:  # mat 에서 이미 지나간 경우(1)이면 pass
      pass 
    
print(cnt)