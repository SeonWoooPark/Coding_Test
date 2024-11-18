# 문제 1. 유기농 배추
# from collections import deque
# t = int(input())
# result_list = []
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# def bfs(i, j):
#     q = deque()
#     q.append((i, j))
#     visited[i][j] = True
#     while q:
#         row, col = q.popleft()
#         for i in range(4):
#             nr = row + dr[i]
#             nc = col + dc[i]
#             if 0 <= nr < r and 0 <= nc < c:
#                 if graph[nr][nc] == 1 and not visited[nr][nc]:
#                     visited[nr][nc] = True
#                     q.append((nr, nc))
#
#     return 1
#
#
# for _ in range(t):
#     c, r, n = map(int, input().split())
#     graph = [[0]*c for _ in range(r)]
#     for _ in range(n):
#         col, row = map(int, input().split())
#         graph[row][col] = 1
#
#     visited = [[False] * c for _ in range(r)]
#     cnt = 0
#     for i in range(r):
#         for j in range(c):
#             if graph[i][j] == 1 and not visited[i][j]:
#                 cnt += bfs(i, j)
#
#     result_list.append(cnt)
#
# for data in result_list:
#     print(data)


# 문제 2. 토마토 (백준 BFS 유형)
# -> row와 col이 큰 Matrix에 대해서는 deepcopy함수와 반복문 전체를 돌며 탐색하는 것은 시간 복잡도가 높기 때문에 방문 그래프와 queue를 이용하여 BFS 탐색을 하자.
# from collections import deque
# c, r = map(int, input().split())
# board = []
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# one_q = deque()
# day = 0
# visited = [[False] * c for _ in range(r)]
# for i in range(r):
#     board.append(list(map(int, input().split())))
#     for j in range(c):
#         if board[i][j] == 1:
#             one_q.append((i, j))
#
# while one_q:
#     next_q = deque()
#     while one_q:
#         row, col = one_q.popleft()
#         for i in range(4):
#             nr = row + dr[i]
#             nc = col + dc[i]
#             if 0 <= nr < r and 0 <= nc < c:
#                 if board[nr][nc] == 0:
#                     visited[nr][nc] = True
#                     board[nr][nc] = 1
#                     next_q.append((nr, nc))
#
#     if next_q:
#         day += 1
#         one_q = next_q
#     else:
#         break
#
# zero_count = 0
# for i in range(r):
#     zero_count += board[i].count(0)
#
# if zero_count != 0:
#     day = -1
# print(day)

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



