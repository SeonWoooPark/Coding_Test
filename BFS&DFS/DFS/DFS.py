# 문제 1. 바이러스 (백준 DFS 유형)
# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n+1)]
# # graph_edge = []
#
# for _ in range(m):
#     # graph_edge.append(list(map(int, input().split())))
#     start, end = map(int, input().split())
#     graph[start].append(end)
#     graph[end].append(start)
#
# for i in range(1, n+1):
#     graph[i].sort()
#
#
# def dfs(graph, v, visited):
#     global cnt
#     visited[v] = True
#     # print(v, end=' ')
#     cnt += 1
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#
# # print(graph)
# visited = [False] * (n+1)
# cnt = -1
# dfs(graph, 1, visited)
# print(cnt)

# 문제 2. 단지 번호 붙이기 (백준 DFS 유형)
from collections import deque
n = int(input())
graph = []

for _ in range(n):
    graph_row = list(map(int, input()))
    graph.append(graph_row)

count_list = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[False]*n for _ in range(n)]

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    cnt = 1
    while q:
        row, col = q.popleft()
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if 0 <= nr < n and 0<= nc < n:
                if graph[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    cnt += 1

    return cnt


for r in range(n):
    for c in range(n):
        if graph[r][c] == 1 and not visited[r][c]:
            count_list.append(bfs(r, c))

count_list.sort()
print(len(count_list))
for count in count_list:
    print(count)

# 문제 3. 연결 요소의 개수
# import sys
# def input():
#     return sys.stdin.readline().rstrip()
#
# n, m = map(int, input().split())
# graph = [[]]
# edge_list = []
# cnt = 0
# visited = [False] * (n+1)
# for _ in range(m):
#     start, end = map(int, input().split())
#     edge_tup = tuple((start, end))
#     edge_list.append(edge_tup)
#
# for i in range(1, n+1):
#     connect_list = []
#     for j in range(m):
#         if i in edge_list[j]:
#             connect_v = edge_list[j][0] if edge_list[j][0] != i else edge_list[j][1]
#             connect_list.append(connect_v)
#     graph.append(connect_list)
#
#
# def dfs(graph, v, visited):
#     visited[v] = True
#     for j in graph[v]:
#         if not visited[j]:
#             dfs(graph, j, visited)
#
#     return 1
#
#
# for i in range(1, n+1):
#     if not visited[i]:
#         cnt += dfs(graph, i, visited)
#
# print(cnt)