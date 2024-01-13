## 각 라인에서 가장 높은 방의 넘버
## 라인0: 1 -> 라인1: 7 -> 라인2: 19 -> 라인3: 37 -> 라인4: 61
## 라인 사이 간격: 6 -> 12 -> 18 -> 24 ... 

# 벌집 N번 방 숫자 받기
n = int(input())

last = 0 # last+1: 각 라인의 마지막 넘버
line = 0 # 라인 번호
while True:
  if (last + 1 <= n) & (n <= last + 1 + line*6):
    print(line + 1)
    break
  else:
    last = last + line*6
    line = line + 1