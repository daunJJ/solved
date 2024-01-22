# n개 입력 받기
n = int(input())

# n줄의 수열 입력 받기
num_list = [int(input()) for _ in range(n)]

# 필요한 변수
stack = []
top = 1
print_list = []
res = True

for i in range(n):
    while top <= num_list[i]:
        stack.append(top)
        print_list.append('+')
        top +=1
    if stack[-1] == num_list[i]:
        stack.pop()
        print_list.append('-')
    else:
        print('NO')
        res = False
        break

if res == True:
    for s in print_list:
        print(s)