# 정수의 개수 받기
test = int(input())

# 정수 받기
num_list = list(map(int, input().split()))

# 최소, 최대 출력
min = num_list[0]
max = num_list[0]
for i in range(1, test):
  if (min >  num_list[i]): min = num_list[i]
  elif (max < num_list[i]): max = num_list[i]
print(min, max)