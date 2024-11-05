# 문제 1. 개미 전사
# DP를 탑다운 방식으로 (재귀적)
# n = int(input())
# input_data = list(map(int, input().split()))
#
# result_list = [0] * n
#
# def search_food(array, find_idx, result_list):
#     if find_idx == 0 or find_idx == 1:
#         return array[find_idx]
#
#     if result_list[find_idx - 1] != 0:
#         next_one = result_list[find_idx - 1]
#     else:
#         next_one = search_food(array, find_idx - 1, result_list)
#
#     if result_list[find_idx - 2] != 0:
#         next_two = result_list[find_idx - 2]
#     else:
#         next_two = search_food(array, find_idx - 2, result_list)
#
#     if next_one > next_two + array[find_idx]:
#         result_list[find_idx] = next_one
#     else:
#         result_list[find_idx] = next_two + array[find_idx]
#
#     return result_list[find_idx]
#
# print(search_food(input_data, n-1, result_list))

# DP를 보톰업 방식으로 (반복)
# n = int(input())
# array = list(map(int, input().split()))
#
# d = [0] * 100
#
# d[0] = array[0]
# d[1] = max(array[0], array[1])
#
# for i in range(2, n):
#     d[i] = max(d[i-1], d[i-2] + array[i])
#
# print(d[n-1])

# 문제 2. 1로 만들기
# n = int(input())
# d = [0] * (n + 1)
#
# for i in range(2, n+1):
#     d[i] = d[i-1] + 1
#     # if i % 5 == 0:
#     #     d[i] = min(d[i], d[i//5] + 1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i//3] + 1)
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i//2] + 1)
#
#
# print(d[n])

# 문제 3. 효율적인 화폐 구성
# n, m = map(int, input().split())
#
# coin_list = []
# for _ in range(n):
#     coin_list.append(int(input()))
#
# d = [-1] * (m + 1)
# d[0] = 0
# start = min(coin_list)
#
#
# for i in range(start, m+1):
#     for coin in coin_list:
#         if i >= coin and d[i-coin] >= 0:
#             d[i] = min(d[i-coin] + 1, d[i]) if d[i] != -1 else d[i-coin] + 1
#
# print(d[m])

# 문제 4. 금광
# T = int(input())
# for test in range(T):
#     r, c = map(int, input().split())
#
#     gold_data = list(map(int, input().split()))
#     gold = [gold_data[c*i:c*(i+1)] for i in range(r)]
#     dr = [-1, 0, 1]
#
#     d = [[0] * c for _ in range(r)]
#     for i in range(r):
#         d[i][0] = gold[i][0]
#
#     for col in range(1, c):
#         for row in range(0, r):
#             for i in range(3):
#                 nr = row + dr[i]
#                 nc = col - 1
#                 if 0 <= nr < r and 0 <= nc < c:
#                     d[row][col] = max(d[row][col], d[nr][nc]+gold[row][col])
#
#     max_value = max([d[i][c-1] for i in range(r)])
#     print(max_value)

# 문제 5. 병사 배치하기
#LIS로 해결
# n = int(input())
# sol_list = list(map(int, input().split()))
# sol_list.reverse()
#
# d = [1] * n
#
# for i in range(1, n):
#     for j in range(0, i):
#         if sol_list[i] > sol_list[j]:
#             d[i] = max(d[j]+1, d[i])
#
# print(n-max(d))

# LDS로 해결
# n = int(input())
# sol_list = list(map(int, input().split()))
#
# d = [1]*n
# for i in range(1, n):
#     for j in range(0,i):
#         if sol_list[j] >= sol_list[i]:
#             d[i] = max(d[j]+1, d[i])
#
# print(n-max(d))

# 문제 6. 1, 2, 3 더하기
# T = int(input())
# result_list = []
# for _ in range(T):
#     n = int(input())
#
#     if n == 1:
#         result_list.append(1)
#     elif n == 2:
#         result_list.append(2)
#     elif n == 3:
#         result_list.append(4)
#     else:
#         dp = [0] * n
#         dp[0] = 1
#         dp[1] = 2
#         dp[2] = 4
#         for i in range(3, n):
#             dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
#         result_list.append(dp[n-1])
#
# for data in result_list:
#     print(data)

# 문제 7. 피보나치 함수
# T = int(input())
# result_list = []
# for _ in range(T):
#     n = int(input())
#     if n == 0:
#         result_list.append([1, 0])
#     elif n == 1:
#         result_list.append([0, 1])
#     else:
#         dp = [[0]*2 for _ in range(n+1)]
#         dp[0] = [1, 0]
#         dp[1] = [0, 1]
#         for i in range(2, n+1):
#             dp[i][0] = dp[i-1][0] + dp[i-2][0]
#             dp[i][1] = dp[i-1][1] + dp[i-2][1]
#
#         result_list.append(dp[n])
#
# for data in result_list:
#     print(data[0], data[1])

# 문제 8. 2xn 타일링
# n = int(input())
# dp = [0] * n
# result = 0
#
# if n == 1:
#     result = 1
# elif n == 2:
#     result = 2
# else:
#     dp[0] = 1
#     dp[1] = 2
#     for i in range(2, n):
#         dp[i] = dp[i-1] + dp[i-2]
#
#     result = dp[n-1]
#
# print(result%10007)

# 문제 9. 피보나치 수
# n = int(input())
# dp = [0] * n
# result = 0
#
# if n == 1 or n == 2:
#     result = 1
# else:
#     dp[0] = 1
#     dp[1] = 1
#     for i in range(2, n):
#         dp[i] = dp[i-1] + dp[i-2]
#
#     result = dp[n-1]
#
# print(result)

# 문제 10. 가장 긴 증가하는 부분 수열 4
n = int(input())
a = list(map(int, input().split()))
dp = [[x] for x in a]

for i in range(1, n):
    for j in range(0, i):
        if a[i] > a[j] and len(dp[j]) + 1 > len(dp[i]):
            dp[i] = dp[j] + [a[i]]

max_idx = 0
max_len = 0
for i in range(n):
    if max_len < len(dp[i]):
        max_len = len(dp[i])
        max_idx = i

print(max_len)
for data in dp[max_idx]:
    print(data, end=' ')