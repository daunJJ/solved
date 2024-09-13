croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for s in croatia:
  if s in word:
    word = word.replace(s, '*')  # 크로아티아 알파벳에 포함되면 1글자의 특수문자로 바꿈 

print(len(word))