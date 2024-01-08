# 테스트 케이스 개수 받기
test = int(input())

# OX결과를 리스트로 받기 
ox_list = [input() for _ in range(test)]

# 각 케이스의 점수 계산하기
for i in range(test):
  cont = 0  # 연속된 O의 개수를 세는 용도
  score = 0  # 점수 계산 용도
  for j in range(len(ox_list[i])):
    if ox_list[i][j] == 'O':  # O 일 때
      cont = cont + 1  # 연속된 O의 개수 세기
      score = score + cont  
    else:  # X 일 때
      cont = 0
  print(score)