# 입력 받기 
num_list = [int(input()) for _ in range(3)]

# 곱하기 
multi = num_list[0] * num_list[1] * num_list[2]

# 0 ~ 9 숫자의 개수 세기
count_list = []

for i in range(0,10):
  count_list.append(list(str(multi)).count(str(i)))
  print(count_list[i])