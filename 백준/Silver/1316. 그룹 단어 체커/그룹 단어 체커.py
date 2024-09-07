# 입력 단어의 개수 받기
N = int(input())

cnt = 0  # 그룹 단어 Count

for i in range(N): 
  word = input()  # 단어 받기 
  word_unique = []  # 이미 등장한 단어인지 확인 용도
  pre = ''  # 직전 단어와 일치하는지 확인 용도 
  group=True # 그룹단어 여부 
  for j in range(len(word)):
    if (word[j] != pre) & (word[j] in word_unique):  # 직전 단어와 동일하지 않은데, 이미 등장한 단어이면 -> 그룹 단어 조건 탈락
      group=False
      break
    else:
      if word[j] not in word_unique:  # 처음 등장한 단어이면 -> word_unique에 저장 
        word_unique.append(word[j])
      else:  # 처음 등장한 단어가 아니면 -> 직전 단어와 동일하다는 의미이므로 Pass 
        pass
    pre = word[j]  # 현재 단어를 직전 단어로 지정 
  if group==True: # 그룹 조건 만족
    cnt += 1
    
print(cnt)