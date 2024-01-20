# 단어의 개수 N 입력 받기
n = int(input())

# 단어 입력 받아 리스트로 저장
str_list = [input() for _ in range(n)]

# 중복 제거
str_list = list(set(str_list))

# 우선 단어 리스트를 알파벳순으로 정렬
str_list.sort()

# 단어의 길이를 리스트로 저장 
len_str = list()
for i in range(len(str_list)):
  len_str.append(len(str_list[i]))

# 길이가 짧은 것부터 출력
for len_ in sorted(list(set(len_str))):  # 존재하는 단어의 길이를 순환하며
  for i in range(len(str_list)):  # 짧은 것부터 해당하는 단어 출력
    if (len_str[i] == len_):
      print(str_list[i])