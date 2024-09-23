# 정점 개수, 간선 개수, 탐색 시작 정점 번호 받기
N, M, V = map(int, input().split())

# 양방향 그래프 생성 (모든 노드 포함 보장)
graph = {i: [] for i in range(1, N+1)}  # 1부터 N까지의 노드를 모두 포함

for i in range(M): 
    S, E = map(int, input().split())
    graph[S].append(E)
    graph[E].append(S)

# 정점 번호를 오름차순으로 정렬
for key in graph.keys():
    graph[key].sort()

# DFS (깊이 우선 탐색)
node = V  # 시작 노드 
visited = [V]  # 방문한 노드 
stack = [V]  # 현재 위치 
end_point = False 

while True: 
    if len(visited) == N:  # end_point1 : 모든 노드 탐색 
        end_point = True
    if end_point == True:
        break
    open = sorted(list(set(graph[node]) - set(visited)))  # 현 노드의 연결 노드 중 방문 안 한 노드만 open 
    if len(open) != 0:  # 방문 안한 노드 존재 
        node = open[0]   # 번호가 가장 작은 노드 방문 
        visited.append(node)
        stack.append(node)  # 현재 위치 업데이트
    else:  # 모든 노드 방문 
        stack.pop()  # 현재 노드 pop 
        if len(stack) == 0:  # end_point2: 남은 탐색 경로 없음 
            end_point = True 
        else: 
            node = stack[-1]  # 과거 노드로 이동 

for num in visited:
    print(num, end=' ')
print('')

# BFS (너비 우선 탐색)
node = V  # 시작 노드 
visited = [V]  # 방문한 노드 
queue = [V]  # 현재 위치 
end_point = False 

while True:
    if len(visited) == N:  # end_point1 : 모든 노드 탐색 
        end_point = True
    if end_point == True:
        break
    node = queue.pop(0)  # 현재 위치 pop 
    open = sorted(list(set(graph[node]) - set(visited)))  # 현 노드의 연결 노드 중 방문 안 한 노드만 open 
    if len(open) != 0:  # 방문 안한 노드 존재 
        visited = visited + open  # open한 노드를 모두 방문
        queue = queue + open  # 현재 위치 업데이트
    else:  # 모든 노드 방문
        if len(queue) == 0:  # end_point2: 남은 탐색 경로 없음 
            end_point = True 
        else:
            node = queue[0]  # 다음 노드로 이동 

for num in visited:
    print(num, end=' ')