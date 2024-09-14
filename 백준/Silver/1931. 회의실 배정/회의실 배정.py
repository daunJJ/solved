N = int(input())

# N개의 회의에 대한 (시작 시간, 종료 시간) 받기
meeting = []
for i in range(N):
  s, e = map(int, input().split())
  meeting.append((s, e))

# 회의 종료 시간이 빠른 것부터 배정할 것임 -> 그리디 (현 시점의 최적 찾기)
meeting.sort(key=lambda x: (x[1], x[0]))

cnt = 0  # 배정된 회의 세기
end_time = 0  # 종료 시간 초기화 

# 순차적으로 현 시점에서 종료 시간이 빠른 것부터 배정 
for i in range(len(meeting)):
  if meeting[i][0] >= end_time:  # 다음 회의의 시작 시간 > 전 회의의 종료 시간 이면 배정
    end_time = meeting[i][1]  # 해당 회의의 종료 시간 가져오기 
    cnt += 1  # 배정된 회의 + 1
  
print(cnt)