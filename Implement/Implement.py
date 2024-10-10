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



