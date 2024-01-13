# 두 수  입력 받기
a, b = map(int, input().split())

# 최대공약수 구하기: 유클리드 호제법 이용 
def gcm(a, b):
  if (a % b == 0):
    return b
  else:
    return gcm(b, a % b)

print(gcm(a,b))
  
# 최소공배수 구하기: 최대공약수 이용
lcm = gcm(a,b) * (a // gcm(a,b)) * ( b // gcm(a,b))
print(lcm)