# 10개 숫자 입력받기
num_list = [int(input()) for _ in range(10)]

# 42로 나눈 나머지를 저장하는 리스트
extra = [i%42 for i in num_list]

# 나머지 리스트에서 서로 다른 값의 개수 세기
print(len(set(extra)))