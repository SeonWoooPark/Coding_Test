# 문제 1. 바이러스 (백준 DFS 유형)
# n = int(input())
# m = int(input())
# graph = [[]]
# graph_edge = []
#
# for _ in range(m):
#     graph_edge.append(list(map(int, input().split())))
#
# for i in range(1, n+1):
#     connect_list = []
#     for j in range(m):
#         if i in graph_edge[j]:
#             connect_v = graph_edge[j][0] if graph_edge[j][0] != i else graph_edge[j][1]
#             connect_list.append(connect_v)
#
#     connect_list.sort()
#     graph.append(connect_list)
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
#
# visited = [False] * (n+1)
# cnt = -1
# dfs(graph, 1, visited)
# print(cnt)

# 문제 2. 단지 번호 붙이기 (백준 DFS 유형)
# n = int(input())
# graph = []
#
# for _ in range(n):
#     graph_row = list(map(int, input()))
#     graph.append(graph_row)
#
# count_list = []
# label = 2
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# def dfs(r, c, cnt):
#     global graph, dr, dc, label
#     graph[r][c] = label
#     cnt += 1
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < n and 0 <= nc < n and graph[nr][nc] == 1:
#             cnt = dfs(nr, nc, cnt)
#
#     return cnt
#
# for r in range(n):
#     for c in range(n):
#         if graph[r][c] == 1:
#             cnt = 0
#             count_list.append(dfs(r, c, cnt))
#             label += 1
#
# count_list.sort()
# print(label-2)
# for count in count_list:
#     print(count)

# 문제 3. 연결 요소의 개수
import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[]]
edge_list = []
cnt = 0
visited = [False] * (n+1)
for _ in range(m):
    start, end = map(int, input().split())
    edge_tup = tuple((start, end))
    edge_list.append(edge_tup)

for i in range(1, n+1):
    connect_list = []
    for j in range(m):
        if i in edge_list[j]:
            connect_v = edge_list[j][0] if edge_list[j][0] != i else edge_list[j][1]
            connect_list.append(connect_v)
    graph.append(connect_list)


def dfs(graph, v, visited):
    visited[v] = True
    for j in graph[v]:
        if not visited[j]:
            dfs(graph, j, visited)

    return 1


for i in range(1, n+1):
    if not visited[i]:
        cnt += dfs(graph, i, visited)

print(cnt)