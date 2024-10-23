# 음료수 얼려 먹기
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

# BFS를 사용한 미로 탈출
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and (nx != 0 or ny != 0):
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0, 0))

for i in range(n):
    for j in range(m):
        print(graph[i][j], end=' ')
    print()

