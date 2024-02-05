while True:
  string = input()
  if string == '.':
    break
  else:
    strlist = []  # (), []를 담는 리스트
    for i in string:
      # []
      if (i  == '[') :  # 1. 괄호가 열리면
        strlist.append(i)   # 1-1. 리스트에 추가
      elif (i == ']') :  # 2. 괄호가 닫히면
        if len(strlist) == 0:  # 2-1. [ 가 없는 경우
          strlist.append(i)
          break
        elif strlist[-1] == '[':  # 2-2. [ 가 있는 경우
          strlist.pop()  # 리스트에 있던 [ 를 pop
        else:  # 2-3. 그외의 경우 
          break
      # ()
      elif (i == '('):
        strlist.append(i)
      elif (i == ')'):
        if len(strlist) == 0:
          strlist.append(i)
          break
        elif strlist[-1] == '(':
          strlist.pop()
        else:
          break
    if len(strlist) == 0:  # 균형이 잡힌 경우는 전부 pop되어 빈 list가 됨
      print("yes")
    else:
      print("no")