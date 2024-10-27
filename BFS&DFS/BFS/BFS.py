# 문제 1. 유기농 배추
# from collections import deque
#
# t = int(input())
# num_list = []
#
# def bfs(row, col):
#     global graph, label, r, c
#     graph[row][col] = label
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#
#     queue = deque()
#     queue.append((row,col))
#     while queue:
#         pos_r, pos_c = queue.popleft()
#         for i in range(4):
#             nr = pos_r + dr[i]
#             nc = pos_c + dc[i]
#             if 0 <= nr < r and 0 <= nc < c and graph[nr][nc] == 1:
#                 graph[nr][nc] = label
#                 queue.append((nr, nc))
#
#     label += 1
#
# for _ in range(t):
#     r, c, n = map(int, input().split())
#     label = 2
#     graph = [[0]*c for _ in range(r)]
#     for _ in range(n):
#         r_pos, c_pos = map(int, input().split())
#         graph[r_pos][c_pos] = 1
#
#     for row in range(r):
#         for col in range(c):
#             if graph[row][col] == 1:
#                 bfs(row, col)
#
#     num_list.append(label-2)
#
# for data in num_list:
#     print(data)

# 문제 2. 토마토 (백준 BFS 유형)
# -> row와 col이 큰 Matrix에 대해서는 deepcopy함수와 반복문 전체를 돌며 탐색하는 것은 시간 복잡도가 높기 때문에 방문 그래프와 queue를 이용하여 BFS 탐색을 하자.
# from collections import deque
# import sys
# def input():
#     return sys.stdin.readline().rstrip()
#
# c, r = map(int, input().split())
# graph = []
# visited = [[0]*c for _ in range(r)]
# init_sum = 0
# minus_cnt = 0
# queue = deque()
#
# for i in range(r):
#     graph_row = list(map(int, input().split()))
#     minus_cnt += graph_row.count(-1)
#     init_sum += sum(graph_row)
#     for j in range(c):
#         if graph_row[j] == 1:
#             queue.append((i, j))
#     graph.append(graph_row)
#
# day = 0
# prev_sum = -1
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# while True:
#     if prev_sum == init_sum:
#         print(-1)
#         break
#     elif init_sum + (2*minus_cnt) == r * c:
#         print(day)
#         break
#
#     new_queue = deque()
#     prev_sum = init_sum
#     while queue:
#         row, col = queue.popleft()
#         for i in range(4):
#             nr = row + dr[i]
#             nc = col + dc[i]
#             if 0 <= nr < r and 0 <= nc < c and graph[nr][nc] == 0 and not visited[nr][nc]:
#                 graph[nr][nc] = 1
#                 visited[nr][nc] = 1
#                 init_sum += 1
#                 new_queue.append((nr, nc))
#
#     queue = new_queue
#     day += 1

# 문제 3. 미로 탐색
# from collections import deque
# r, c = map(int, input().split())
# graph = []
# visited = []
# for _ in range(r):
#     graph_row = list(map(int, input()))
#     graph.append(graph_row)
#     visited_row = [False]*c
#     visited.append(visited_row)
#
# def bfs(graph, row, col, visited):
#     global r, c
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#     visited[row][col] = True
#     queue = deque()
#     queue.append((row, col))
#     while queue:
#         pos_r, pos_c = queue.popleft()
#         for i in range(4):
#             nr = pos_r + dr[i]
#             nc = pos_c + dc[i]
#             if 0 <= nr < r and 0 <= nc < c and graph[nr][nc] == 1 and not visited[nr][nc]:
#                 visited[nr][nc] = True
#                 graph[nr][nc] = graph[pos_r][pos_c] + 1
#                 queue.append((nr, nc))
#
#     return graph[r-1][c-1]
#
# print(bfs(graph, 0, 0, visited))



