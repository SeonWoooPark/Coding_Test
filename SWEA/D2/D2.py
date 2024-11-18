# 문제 1. 달팽이 숫자
# n = int(input())
# array = [[0] * n for _ in range(n)]
# start = 1
# depth = 0
#
# def fill_num(array, n, start, depth):
#     if n == depth:
#         return
#
#     for i in range(depth, n-depth):
#         array[depth][i] = start
#         start += 1
#     start -= 1
#
#     for i in range(depth, n-depth):
#         array[i][n-depth-1] = start
#         start += 1
#     start -= 1
#
#     for i in range(n-depth-1, depth-1, -1):
#         array[n-depth-1][i] = start
#         start += 1
#     start -= 1
#
#     for i in range(n-depth-1, depth, -1):
#         array[i][depth] = start
#         start += 1
#     depth += 1
#     fill_num(array, n, start, depth)
#
# fill_num(array, n, start, depth)
#
# print(f'#{test_case}')
# for i in range(n):
#     for j in range(n):
#         print(array[i][j], end=' ')
#     print()

