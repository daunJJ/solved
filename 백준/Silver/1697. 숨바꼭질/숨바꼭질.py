from collections import deque

# 수빈이와 동생의 위치 받기
N, K = map(int, input().split())

# 너비우선 탐색 코드 구현 
def DFS(N, K):
    # 초기화 
    pre = (N, 0)  # (위치, 시간)
    queue = deque([pre])  # deque를 사용하여 큐 구현
    visited = set()  # 위치만 저장 

    while queue:
        pre = queue.popleft()
        visited.add(pre[0])  # 방문한 위치 저장 

        if pre[0] == K:  # 성공 조건
            print(pre[1])  # 걸린 시간 출력
            return

        # 이동 가능한 세 방향 탐색
        for n in (pre[0] - 1, pre[0] + 1, pre[0] * 2):
            if 0 <= n <= 100000 and n not in visited:
                queue.append((n, pre[1] + 1))  # (방문가능한 위치, 현재까지 걸린 시간)

DFS(N, K)