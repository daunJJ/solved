# 단어 받기
s = input()

# 26개 알파벳 문자열
alpha = 'abcdefghijklmnopqrstuvwxyz'

# 단어에서 알파벳 위치 찾기
for i in range(len(alpha)):
  print(s.find(alpha[i]), end=' ')