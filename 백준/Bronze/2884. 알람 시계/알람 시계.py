# H시 M분 입력 받기
H, M = map(int, input().split())

# 45분 이른 시각 구하기
if M >= 45:
  M = M - 45
else:
  H = H - 1
  M = M + 60 - 45
  if H == -1:  # 0시 인 경우 예외 처리 필요
    H = 23

print(H,M)