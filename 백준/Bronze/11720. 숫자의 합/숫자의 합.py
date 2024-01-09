# 숫자의 개수 받기
cnt = int(input())

# 개수만큼 숫자 받기
num = input()

# 숫자 모두 더하기
sum = 0
for i in range(cnt):
  sum = sum + int(num[i])

print(sum)