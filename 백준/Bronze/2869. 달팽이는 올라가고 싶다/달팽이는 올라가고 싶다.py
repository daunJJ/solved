# 낮에 올라가는 거리, 밤에 미끄러지는 거리, 나무 막대 총 길이
a, b, v = map(int, input().split())

# (나무 막대 총 길이 - 미끄러지는 거리) // (올라가는 거리 - 미끄러지는 거리)
if ( (v - b) // (a - b) == (v - b) / (a - b) ):
  print((v - b) // (a - b))
else:
  print((v - b) // (a - b)+1)