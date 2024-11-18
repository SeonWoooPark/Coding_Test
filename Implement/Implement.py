# 문제 1. 상하좌우 -> 시뮬레이션 문제
# n = int(input())
# input_move = input().split()
#
# x, y = 1, 1
#
# # 상, 하, 좌, 우 -> 방향벡터 사용
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# for dir in input_move:
#     if dir == 'U' and x > 1:
#         x += dx[0]
#         y += dy[0]
#     elif dir == 'D' and x < n:
#         x += dx[1]
#         y += dy[1]
#     elif dir == 'L' and y > 1:
#         x += dx[2]
#         y += dy[2]
#     elif dir == 'R' and y < n:
#         x += dx[3]
#         y += dy[3]
#
# print(x, y)

# 문제 2. 시각 -> 완전 탐색 유형
# n = int(input())
# count = 0
#
# # 전부 탐색
# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             time = str(i) + str(j) + str(k)
#             if '3' in time:
#                 count += 1
#
# print(count)

# 문제 3. 왕실의 나이트 -> 완전 탐색
# input_ = input()
# alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# col = alph.index(input_[0]) + 1
# row = int(input_[1])
# count = 0

# 상좌, 상우, 우상, 우하, 하우, 하좌, 좌하, 좌상
# dcol = [-1, 1, 2, 2, 1, -1, -2, -2]
# drow = [-2, -2, -1, 1, 2, 2, 1, -1]
#
# for i in range(8):
#     next_col = col + dcol[i]
#     next_row = row + drow[i]
#     if next_col >= 1 and next_col <= 8 and next_row >= 1 and next_row <= 8:
#         count += 1
#
# print(count)

# 문제 4. 문자열 재정렬
# input_str = input()
# result_list = []
# result_num = 0
#
# for data in input_str:
#     if data >= 'A' and data <= 'Z':
#         result_list.append(data)
#     else:
#         result_num += int(data)
#
# result_list.sort()
# result_str = "".join(result_list) + str(result_num)
# print(result_str)

# 문제 5. 프린터 큐
# from collections import deque
#
# input_len = int(input())
# result_count = []
#
# for _ in range(input_len):
#     n, find_idx = map(int, input().split())
#     value_print = list(map(int, input().split()))
#     value_tup = [(value_print[i], i) for i in range(len(value_print))]
#     value_queue = deque(value_tup)
#     max_value = max(value_queue)
#     cur_pop = value_queue.popleft()
#     count = 0
#     while True:
#         if max_value[0] == cur_pop[0] and find_idx == cur_pop[1]:
#             count += 1
#             result_count.append(count)
#             break
#         elif max_value[0] == cur_pop[0]:
#             count += 1
#             max_value = max(value_queue)
#             cur_pop = value_queue.popleft()
#         elif max_value != cur_pop[0]:
#             value_queue.append(cur_pop)
#             cur_pop = value_queue.popleft()
#
# for data in result_count:
#     print(data)

# 문제 6. 로봇 청소기
r, c = map(int, input().split())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
board = []
cur_r, cur_c, way = map(int, input().split())

for _ in range(r):
    board.append(list(map(int, input().split())))

cnt = 0
while True:
    if board[cur_r][cur_c] == 0:
        cnt += 1
        board[cur_r][cur_c] = 2

    prev_r = cur_r
    prev_c = cur_c

    for i in range(1, 5):
        nway = (way-i) % 4
        nr = cur_r + dr[nway]
        nc = cur_c + dc[nway]
        if 0 <= nr < r and 0 <= nc < c and board[nr][nc] == 0:
            cur_r = nr
            cur_c = nc
            way = nway
            break

    if prev_r == cur_r and prev_c == cur_c:
        back_way = (way - 2) % 4
        nr = cur_r + dr[back_way]
        nc = cur_c + dc[back_way]
        if 0 <= nr < r and 0 <= nc < c and board[nr][nc] != 1:
            cur_r = nr
            cur_c = nc
        elif 0 <= nr < r and 0 <= nc < c and board[nr][nc] == 1:
            break

print(cnt)

# 문제 7. 뱀
# from collections import deque
#
# board_len = int(input())
# board = [[0]*board_len for _ in range(board_len)]
# apple_len = int(input())
#
# for _ in range(apple_len):
#     apple_row, apple_col = map(int, input().split())
#     board[apple_row-1][apple_col - 1] = 1
#
# change_len = int(input())
# change_list = []
# for _ in range(change_len):
#     time, way = input().split()
#     time = int(time)
#     change_list.append(tuple([time, way]))
#
# change_que = deque(change_list)
#
# snake = [[0,0]]
# snake_que1 = deque(snake)
# row = 0
# col = 0
# time = 0
# way = 0
# dcol = [1, 0, -1, 0]
# drow = [0, 1, 0, -1]
# is_exist = False
#
# while True:
#     row += drow[way]
#     col += dcol[way]
#     time += 1
#
#     if 0 <= row < board_len and 0 <= col < board_len:
#         snake_body_len = len(snake_que1)
#         for _ in range(snake_body_len):
#             body = snake_que1.popleft()
#             if body[0] == row and body[1] == col:
#                 is_exist = True
#                 break
#             else:
#                 snake_que1.append(body)
#
#         if is_exist:
#             break
#
#         if board[row][col] == 1:
#             snake_que1.append([row,col])
#             board[row][col] = 0
#
#         else:
#             snake_que1.append([row,col])
#             snake_que1.popleft()
#
#         if len(change_que) > 0:
#             change_time = change_que.popleft()
#             if time == change_time[0]:
#                 if change_time[1] == 'L':
#                     way = (way-1) % 4
#                 else:
#                     way = (way + 1) % 4
#
#             else:
#                 change_que.appendleft(change_time)
#
#     else:
#         break
#
# print(time)

# 문제 8. 미세먼지 안녕!
# import copy
# r, c, t = map(int, input().split())
# board = []
# drow = [-1, 0, 1, 0]
# dcol = [0, 1, 0, -1]
#
# for _ in range(r):
#     board_row = list(map(int, input().split()))
#     board.append(board_row)
#
# cleaner_up_row = -1
# cleaner_down_row = -1
# for i in range(r):
#     if i == 0 or i == 1:
#         continue
#     if board[i][0] == -1 and board[i-1][0] != -1:
#         cleaner_up_row = i
#     elif board[i][0] == -1 and board[i-1][0] == -1:
#         cleaner_down_row = i
#         break
#
# for _ in range(t):
#     board_copy = copy.deepcopy(board)
#     for row in range(r):
#         for col in range(c):
#             dif_around = board_copy[row][col] // 5
#             if dif_around > 0:
#                 around_list = []
#                 for i in range(4):
#                     n_row = row + drow[i]
#                     n_col = col + dcol[i]
#                     if 0 <= n_row < r and 0 <= n_col < c:
#                         if board[n_row][n_col] != -1:
#                             around_list.append([n_row, n_col])
#
#                 for i in range(len(around_list)):
#                     board[around_list[i][0]][around_list[i][1]] += dif_around
#                     board[row][col] -= dif_around
#
#     for i in range(cleaner_up_row-1, 0, -1):
#         board[i][0] = board[i-1][0]
#
#     for i in range(c-1):
#         board[0][i] = board[0][i+1]
#
#     for i in range(cleaner_up_row):
#         board[i][c-1] = board[i+1][c-1]
#
#     for i in range(c-1, 1, -1):
#         board[cleaner_up_row][i] = board[cleaner_up_row][i-1]
#
#     board[cleaner_up_row][1] = 0
#
#     for i in range(cleaner_down_row+1, r-1):
#         board[i][0] = board[i+1][0]
#
#     for i in range(c-1):
#         board[r-1][i] = board[r-1][i+1]
#
#     for i in range(r-1, cleaner_down_row, -1):
#         board[i][c-1] = board[i-1][c-1]
#
#     for i in range(c-1, 1, -1):
#         board[cleaner_down_row][i] = board[cleaner_down_row][i-1]
#
#     board[cleaner_down_row][1] = 0
#
# result = 2
# for row in range(r):
#     for col in range(c):
#         result += board[row][col]
#
#
# print(result)

# 문제 9. 치즈
# from collections import deque
#
# r, c = map(int, input().split())
# board = []
# time = 1
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
# sum_c = 0
#
# for _ in range(r):
#     board_row = list(map(int, input().split()))
#     sum_c += sum(board_row)
#     board.append(board_row)
#
#
# while True:
#     visited = [[0] * c for _ in range(r)]
#     q = deque([(0,0)])
#     melt = deque([])
#     while q:
#         cur_r, cur_c = q.popleft()
#         for i in range(4):
#             nr = cur_r + dr[i]
#             nc = cur_c + dc[i]
#             if 0 <= nr < r and 0 <= nc < c and not visited[nr][nc]:
#                 visited[nr][nc] = 1
#                 if board[nr][nc] == 0:
#                     q.append((nr, nc))
#                 elif board[nr][nc] == 1:
#                     melt.append((nr, nc))
#     melt_cnt = 0
#     for cur_r, cur_c in melt:
#         board[cur_r][cur_c] = 0
#         melt_cnt += 1
#
#     sum_c -= melt_cnt
#
#     if sum_c == 0:
#         print(time, melt_cnt, sep="\n")
#         break
#
#     time += 1


# 문제 10. 빗물
# from collections import deque
#
# h, w = map(int, input().split())
# board = list(map(int, input().split()))
#
# cnt = 0
# for i in range(1, w-1):
#     left_max = max(board[:i])
#     right_max = max(board[i+1:])
#
#     compare_min = min(left_max, right_max)
#
#     if board[i] < compare_min:
#         cnt += compare_min - board[i]
#
# print(cnt)


# 문제 11. 테트르미노
# n, m = map(int, input().split())
# graph = []
# visited = [[False] * m for _ in range(n)]
# maximum = 0
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# for _ in range(n):
#     graph.append(list(map(int, input().split())))
#
#
# def dfs(r, c, tmp, cnt):
#     global maximum
#     if cnt == 4:
#         maximum = max(maximum, tmp)
#     else:
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
#                 visited[nr][nc] = True
#                 dfs(nr, nc, tmp + graph[nr][nc], cnt + 1)
#                 visited[nr][nc] = False
#
#     return
#
#
# def fly(r, c, tmp):
#     global maximum
#     pos = []
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < n and 0 <= nc < m:
#             pos.append(graph[nr][nc])
#
#     if len(pos) == 4:
#         pos.sort(reverse=True)
#         pos.pop()
#         maximum = max(maximum, tmp + sum(pos))
#     elif len(pos) == 3:
#         maximum = max(maximum, tmp + sum(pos))
#
#     return
#
# for i in range(n):
#     for j in range(m):
#         visited[i][j] = True
#         dfs(i, j, graph[i][j], 1)
#         fly(i, j, graph[i][j])
#         visited[i][j] = False
#
# print(maximum)

# 문제 12. 아기 상어
# from collections import deque
# import heapq
#
# n = int(input())
# graph = []
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# eat_que = deque()
#
# sz = 2
# time = 0
# eat_cnt = 0
#
# cur_pos = (-1, -1)
#
# for i in range(n):
#     graph_row = list(map(int, input().split()))
#     graph.append(graph_row)
#     for j in range(n):
#         if 0 < graph_row[j] < sz:
#             eat_que.append((i, j))
#         elif graph_row[j] == 9:
#             cur_pos = (i, j)
#
#
# def bfs(cur_pos, e_r, e_c):
#     visited = [[0] * n for _ in range(n)]
#     q = deque()
#     q.append(cur_pos)
#
#     while q:
#         r, c = q.popleft()
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
#                 if graph[nr][nc] != 9 and graph[nr][nc] <= sz:
#                     visited[nr][nc] = visited[r][c] + 1
#                     q.append((nr, nc))
#
#     return visited[e_r][e_c]
#
#
# while True:
#     distance = []
#     if eat_que:
#         while eat_que:
#             e_r, e_c = eat_que.popleft()
#             dist = bfs(cur_pos, e_r, e_c)
#             if dist != 0:
#                 heapq.heappush(distance, (dist, (e_r, e_c)))
#
#         if distance:
#             dist_data = heapq.heappop(distance)
#             min_dist = dist_data[0]
#             graph[cur_pos[0]][cur_pos[1]] = 0
#             nr, nc = dist_data[1][0], dist_data[1][1]
#             cur_pos = (nr, nc)
#             graph[cur_pos[0]][cur_pos[1]] = 9
#             time += min_dist
#             eat_cnt += 1
#             if eat_cnt == sz:
#                 sz += 1
#                 eat_cnt = 0
#                 for i in range(n):
#                     for j in range(n):
#                         if graph[i][j] != 9 and 0 < graph[i][j] < sz:
#                             eat_que.append((i, j))
#             else:
#                 for data in distance:
#                     eat_que.append(data[1])
#     else:
#         print(time)
#         break

# 문제 13. 단어 뒤집기2
# result = ''
# s = input()
# isTag = False
# buffer_s = ''
#
# for c in s:
#     if isTag:
#         if c == '>':
#             isTag = False
#         result += c
#     else:
#         if c == ' ':
#             bf_list = list(buffer_s)
#             bf_list.reverse()
#             result += ''.join((bf_list))
#             result += ' '
#             buffer_s = ''
#         elif c == '<':
#             bf_list = list(buffer_s)
#             bf_list.reverse()
#             result += ''.join((bf_list))
#             result += '<'
#             buffer_s = ''
#             isTag = True
#         else:
#             buffer_s += c
#
# bf_list = list(buffer_s)
# bf_list.reverse()
# result += ''.join((bf_list))
# print(result)

# 문제 14. 마인크래프트
# r, c, b = map(int, input().split())
# graph = []
# result_h = -1
# result_t = int(1e9)
#
# for _ in range(r):
#     graph.append(list(map(int, input().split())))
#
# for i in range(257):
#     sum_height = 0
#     sum_time = 0
#     for row in range(r):
#         for col in range(c):
#             av = i - graph[row][col]
#             if av > 0:
#                 sum_time += av
#             else:
#                 sum_time += (-av) * 2
#             sum_height += av
#
#     if sum_height > b:
#         break
#     else:
#         if result_t > sum_time:
#             result_t = sum_time
#             result_h = i
#         elif result_t == sum_time and result_h < i:
#             result_h = i
#
# print(result_t, result_h)

# 문제 15. 톱니바퀴
# board = [[]]
# rotate = []
# for _ in range(4):
#     board.append(list(map(int, input())))
#
# n = int(input())
# for _ in range(n):
#     rotate.append(tuple(map(int, input().split())))
#
# def rotate_t(t, way):
#     if way == 1:
#         last = t.pop()
#         t.insert(0, last)
#     else:
#         first = t.pop(0)
#         t.append(first)
#
#
# for num, way in rotate:
#     count = 1
#     pre_num = board[num][6]
#     for i in range(num-1, 0, -1):
#         if pre_num != board[i][2]:
#             pre_num = board[i][6]
#             rotate_t(board[i], way * ((-1)**count))
#             count += 1
#         else:
#             break
#
#     count = 1
#     pos_num = board[num][2]
#     for i in range(num+1, 5):
#         if pos_num != board[i][6]:
#             pos_num = board[i][2]
#             rotate_t(board[i], way*((-1)**count))
#             count += 1
#         else:
#             break
#     rotate_t(board[num], way)
#
#
# result = 0
# for i in range(1, 5):
#     result += board[i][0] * (2 ** (i-1))
#
# print(result)
