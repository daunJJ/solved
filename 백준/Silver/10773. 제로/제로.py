# 장부에 적힌 K개의 숫자 받기
K = int(input())

# 장부에 적힌 수의 합 구하기
money_list = []
sum = 0

for i in range(K):
  money = int(input())
  if money == 0:  # 0이 들어오면 
    release = money_list.pop()  # 가장 최근에 들어온 값을 없앰
    sum = sum - release
  else:
    money_list.append(money)  # money 리스트에 추가
    sum = sum + money

print(sum)