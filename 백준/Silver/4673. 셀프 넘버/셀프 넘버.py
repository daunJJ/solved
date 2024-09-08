not_self_num = []  # NOT 셀프넘버 모음

for i in range(1,10000):
  if i not in not_self_num:  #  NOT 셀프넘버 모음에 없음 -> 셀프넘버라는 뜻 
    print(i)
  make_num = i  # 생성: d(n)에서 n 더하기 
  n = str(i)  # 각 자리수를 더하기 위해 문자열로 변환하여 인덱싱 
  for j in range(len(n)):
    make_num += int(n[j])  # 생성: d(n)에서 각 자리수 더하기 
  not_self_num.append(make_num)   # 생성된 수를 NOT 셀프넘버 모음에 추가 