# 배달해야 하는 설탕의 무게 받기
N = int(input())

# 5킬로 설탕의 봉지 수, 3킬로 설탕의 봉지 수 계산하기
# 5보다 클 때 
if  N >= 5:
  for i in range( N//5 , -1 , -1):  # N을 5로 나눈 최대 몫에서 부터 하나씩 줄여가며 5와 3으로 나누어 떨어지는지 확인
    cnt = 0
    remain = N - 5 * i  # 5의 배수로 나눈 나머지
    if remain % 3 == 0:  # 나머지가 3으로 나눠 떨어지면 N킬로 만들 수 있음
      cnt = i + ( remain // 3 )
      break
    else:  
      cnt = -1
# 5보다 작지만 3일 때
elif N == 3:
  cnt = 1
# 5보다 작고 3이 아닐 때
else:
  cnt = -1

print(cnt)