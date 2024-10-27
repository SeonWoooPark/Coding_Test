# 문제 1. 음료수 얼려 먹기 (BFS와 DFS 모두 사용 가능)
#BFS와 visited graph를 사용하여 해결
# from collections import deque
#
# r, c = map(int, input().split())
# ice_board = []
#
# for _ in range(r):
#     board_row = list(map(int, input()))
#     ice_board.append(board_row)
#
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# cnt = 2
#
# def bfs(row, col):
#     global ice_board, dr, dc, r, c, cnt
#     q = deque([(row, col)])
#     visited = [[0] * c for _ in range(r)]
#
#     while q:
#         pop_r, pop_c = q.popleft()
#         for i in range(4):
#             nr = pop_r + dr[i]
#             nc = pop_c + dc[i]
#
#             if 0 <= nr < r and 0 <= nc < c and not visited[nr][nc]:
#                 visited[nr][nc] = 1
#                 if ice_board[nr][nc] == 0:
#                     q.append((nr, nc))
#                     ice_board[nr][nc] = cnt
#
#     cnt += 1
#
#     return
#
# for row in range(r):
#     for col in range(c):
#         if ice_board[row][col] == 0:
#             bfs(row, col)
#
# print(cnt-2)

#DFS와 재귀 호출을 통해 해결하는 코드
# n, m = map(int, input().split())
#
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))
#
# result = 0
# def dfs(x, y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x - 1, y)
#         dfs(x, y - 1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         return True
#     return False
#
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             result += 1
#
# print(result)

# 문제 2. 미로 탈출 (BFS 사용)
# from collections import deque
#
# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs(x, y):
#     queue = deque()
#     queue.append((x,y))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if graph[nx][ny] == 1 and (nx != 0 or ny != 0):
#                     graph[nx][ny] = graph[x][y] + 1
#                     queue.append((nx,ny))
#
#     return graph[n-1][m-1]
#
# print(bfs(0, 0))
#
# for i in range(n):
#     for j in range(m):
#         print(graph[i][j], end=' ')
#     print()

# 문제 3. DFS와 BFS (백준 DFS&BFS 유형)
# from collections import deque
# n, m, v = map(int, input().split())
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
#     connect_list.sort()
#     graph.append(connect_list)
#
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=' ')
#
#     for i in graph[v]:
#         if not visited[i]:
#             visited[i] = True
#             dfs(graph, i, visited)
#
# def bfs(graph, start, visited):
#     queue = deque()
#     queue.append(start)
#     visited[start] = True
#     print(start, end=' ')
#     while queue:
#         v = queue.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#                 print(i, end=' ')
#
#
# visited_dfs = [False] * (n+1)
# visited_bfs = [False] * (n+1)
# dfs(graph, v, visited_dfs)
# print()
# bfs(graph, v, visited_bfs)

