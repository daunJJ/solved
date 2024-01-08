asc = '12345678'
des = '87654321'

a = input().split()

if ''.join(a) == asc:
  print('ascending')
elif ''.join(a) == des:
  print('descending')
else:
    print('mixed')