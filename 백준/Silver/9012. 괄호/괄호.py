# T개의 테스트 개수 받기
t = int(input())

# T개의 테스트 받기
for i in range(t):
  PS = input()
  PS_list = []
  for s in PS:
    if s == '(':  ## 1. ( 일 때
      PS_list.append(s)   # 리스트에 추가
    elif s == ')':  ## 2. ) 일 때
      if len(PS_list) == 0:  # 이전 괄호가 없으면 리스트에 추가 후 break
        PS_list.append(s)
        break
      elif (PS_list[-1] == '(') :  # 이전 괄호가 있으면 리스트에 있는 이전 괄호를 pop
        PS_list.pop()
      else:
        PS_list.append(s)  # 그외 경우엔 리스트에 추가 후 break
        break
    else:  ## 3. 그 외 문자 일 때
      PS_list.append(s)
      break
  if len(PS_list) == 0:  # 정상적인 VPS일 경우 리스트가 모두 pop됨
    print("YES")
  else:
    print("NO")