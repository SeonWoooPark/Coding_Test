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
# all_row, all_col = map(int, input().split())
# row, col, way = map(int, input().split())
# input_data = []
# drow = [-1, 0, 1, 0]
# dcol = [0, 1, 0, -1]
#
# for _ in range(all_row):
#     row_list = list(map(int, input().split()))
#     input_data.append(row_list)
#
# input_data[row][col] = 2
# count = 1
# is_checked = False
# while True:
#     check_v = 0
#     if not(is_checked):
#         for i in range(4):
#             if all_row > row + drow[i] >= 0 and all_col > col + dcol[i] >= 0:
#                 if input_data[row+drow[i]][col+dcol[i]] != 0:
#                     check_v += 1
#             else:
#                 check_v += 1
#
#     if check_v == 4:
#         row += drow[(way+6) % 4]
#         col += dcol[(way+6) % 4]
#         if not(all_row > row >= 0 and all_col > col >= 0):
#             break
#         else:
#             if input_data[row][col] == 1:
#                 break
#
#     else:
#         way = (way - 1) % 4
#         n_row = row+drow[way]
#         n_col = col+dcol[way]
#         if all_row > n_row >= 0 and all_col > n_col >= 0:
#             if input_data[n_row][n_col] == 0:
#                 row = n_row
#                 col = n_col
#                 count += 1
#                 input_data[row][col] = 2
#                 is_checked = False
#         else:
#             is_checked = True
#
# print(count)

# 문제 7. 뱀
from collections import deque

board_len = int(input())
board = [[0]*board_len for _ in range(board_len)]
apple_len = int(input())

for _ in range(apple_len):
    apple_row, apple_col = map(int, input().split())
    board[apple_row-1][apple_col - 1] = 1

change_len = int(input())
change_list = []
for _ in range(change_len):
    time, way = input().split()
    time = int(time)
    change_list.append(tuple([time, way]))

change_que = deque(change_list)

snake = [[0,0]]
snake_que1 = deque(snake)
row = 0
col = 0
time = 0
way = 0
dcol = [1, 0, -1, 0]
drow = [0, 1, 0, -1]
is_exist = False

while True:
    row += drow[way]
    col += dcol[way]
    time += 1

    if 0 <= row < board_len and 0 <= col < board_len:
        snake_body_len = len(snake_que1)
        for _ in range(snake_body_len):
            body = snake_que1.popleft()
            if body[0] == row and body[1] == col:
                is_exist = True
                break
            else:
                snake_que1.append(body)

        if is_exist:
            break

        if board[row][col] == 1:
            snake_que1.append([row,col])
            board[row][col] = 0

        else:
            snake_que1.append([row,col])
            snake_que1.popleft()

        if len(change_que) > 0:
            change_time = change_que.popleft()
            if time == change_time[0]:
                if change_time[1] == 'L':
                    way = (way-1) % 4
                else:
                    way = (way + 1) % 4

            else:
                change_que.appendleft(change_time)

    else:
        break

print(time)







