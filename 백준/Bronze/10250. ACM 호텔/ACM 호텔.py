# 테스트 케이스 개수
test = int(input())

# 호텔의 층 수, 방 수, 몇 번째 손님인지
hotel = [input().split() for _ in range(test)]

# 1번방부터 층수가 올라가면서 배정
# -> 손님의 입장 번호를 층수로 나눈 몫: 방 번호, 손님의 입장 번호를 층수로 나눈 나머지: 층 수
for i in range(test):
  # 맨 윗층이 아닌 경우
  XX = int(hotel[i][2]) // int(hotel[i][0]) + 1  # 방 번호
  YY = int(hotel[i][2]) % int(hotel[i][0])   # 층 수
  # 맨 윗층인 경우 -> 나머지가 0
  if YY == 0:
    XX = int(hotel[i][2]) // int(hotel[i][0])  # 몫 그대로 => 방 번호
    YY = int(hotel[i][0])  # 0층 -> 맨 윗층으로 변경
  # 방 번호가 한 자리 수인 경우 두 자리로 바꾸어야 함
  if XX < 10:
    print(str(YY) + '0' + str(XX))
  else:
    print(str(YY) + str(XX))