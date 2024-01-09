while True:
  num = input()
  if num == '0': break
  num_reverse = ''.join(reversed(list(num)))
  if num == num_reverse: print('yes')
  else: print('no')