word = list(input().upper())

max_cnt = 0
max_str = ''

for i in range(0, len(set(word))):
  pre_cnt = word.count(list(set(word))[i])
  if pre_cnt > max_cnt: 
    max_cnt = pre_cnt
    max_str = list(set(word))[i]
  elif pre_cnt == max_cnt: 
    max_str = '?'

print(max_str)