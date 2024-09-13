not_self_num = []  # NOT 셀프넘버 모음

for num in range(1,10000):
  if num not in not_self_num:  #  NOT 셀프넘버 모음에 없음 -> 셀프넘버라는 뜻 
    print(num)
  for each_num in str(num):  # 생성: d(n)에서 n 더하기
    num += int(each_num)   # 각 자리수를 더하기 위해 문자열로 변환하여 인덱싱 
  not_self_num.append(num)   # 생성된 수를 NOT 셀프넘버 모음에 추가 