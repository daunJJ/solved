import sys

# 리스트로 스택 만들기 
stack = []

# push = stack.append() : 스택에 정수 넣기  
# pop = stack.pop() : 가장 위에 있는 정수 제거
# size = len(stack): 스택에 들어있는 정수 개수 
# empty = not stack : 비어 있으면 True 리턴 
# top = stack[-1] : 스택의 가장 위에 있는 정수 출력 

# 명령의 수 받기
N = int(sys.stdin.readline().rstrip())

# N개의 명령에 대해 명령 수행하기 
for i in range(N):
  # 명령 받기
  inst = sys.stdin.readline().split()
  # push이면 
  if 'push' == inst[0]:
    num =int(inst[1])
    stack.append(num)
  # pop이면 
  elif 'pop' == inst[0]:
    if len(stack) != 0: 
      print(stack.pop())
    else:
      print(-1)
  # size이면 
  elif 'size' == inst[0]:
    print(len(stack))
  # empty이면 
  elif 'empty' == inst[0]:
    print(int(not stack))
  # top이면
  elif 'top' == inst[0]:
    if len(stack) != 0: 
      print(stack[-1])
    else:
      print(-1)