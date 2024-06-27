N = int(input())
meet_time = []; start = []; end = []
# 회의 시작시간, 종료시간을 tuple 형태로 리턴
for _ in range(N):
    meet_time.append(tuple(map(int,input().split())))

# 종료 시간을 기준으로 정렬
# 끝나는 시간이 빠른 회의를 계속 선정 -> 그리디
meet_time.sort(key=lambda meet_time: (meet_time[1], meet_time[0]))

# cnt: 회의 최대 개수
# min_end: 초기 상태에서 가장 빨리 끝나는 시간
cnt = 1; min_end = meet_time[0][1]
# 이미 회의 한 개는 진행
for s_e in meet_time[1:]:
# 현재 종료 시간보다 빠른 경우, 해당 회의 진행 못함
    if s_e[0] < min_end:
        pass
    else:
# 현재 종료 시간보다 시작 시간이 늦은 경우, 해당 회의 진행 가능
    # 최소 종료 시간, 회의 최대 개수 업데이트
        min_end = s_e[1]
        cnt += 1
print(cnt)