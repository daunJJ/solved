n = int(input())

# n이 대각선 몇째줄인지를 찾자
# 1줄: 1/1 -> 1개
# 2줄: 1/2 2/1 - > 2개
# 3줄: 3/1 2/2 1/3 ... -> 3개 

cnt = 1  # 대각선 줄 넘버 = 줄 사이 간격
first = 1  # 궁금한 숫자의 줄 넘버를 찾아가는 용도 

while True:
  if first > n:  # 어떤 줄의 첫번째 숫자가 n보다 커지면 종료 -> 즉 다음 줄을 의미 
    break
  first += cnt  # 각 줄의 첫번째 숫자 
  cnt += 1  # 줄 넘버 + 1 

# 해당 줄의 줄 넘버
line = cnt - 1 
# 해당 줄의 첫번째 분수에 매핑되는 수
start = first - line  # 다음 줄의 첫번째 수 - 해당 줄의 줄 넘버
# n은 해당 줄의 몇 번째 수?
rank = n - start + 1

# 해당 줄의 첫번째 분수로 초기화
num1 = 1
num2 = line

for i in range(1, rank):
  num1 += 1
  num2 -= 1

if line % 2 == 0:  # 대각선 줄 넘버가 짝수이면
  print(str(num1)+'/'+str(num2))
else:  # 대각선 줄 넘버가 홀수이면
  print(str(num2)+'/'+str(num1))