# 문제 1. 떡복이 떡 만들기
# n, m = map(int, input().split())
# height_list = list(map(int, input().split()))
#
# end = max(height_list)
# start = 0
# result = 0
# while start <= end:
#     total = 0
#     mid = (start+end) // 2
#     for x in height_list:
#         if x > mid:
#             total += x - mid
#     if total < m:
#         end = mid - 1
#     elif total > m:
#         result = mid
#         start = mid + 1
#     else:
#         result = mid
#         break
#
# print(result)

# 문제 2. 정렬된 배열에서 특정 수의 개수 구하기
# from bisect import bisect_left, bisect_right
#
# n, x = map(int, input().split())
# sorted_list = list(map(int, input().split()))
#
# left_idx = bisect_left(sorted_list, x)
# right_idx = bisect_right(sorted_list, x)
# result = -1
#
# if left_idx < right_idx:
#     result = right_idx - left_idx
#
# print(result)

# 문제 3. 수 찾기
# from bisect import bisect_left, bisect_right
#
# n = int(input())
# a_list = list(map(int, input().split()))
# a_list.sort()
#
# m = int(input())
# m_list = list(map(int, input().split()))
#
# for data in m_list:
#     left_idx = bisect_left(a_list, data)
#     right_idx = bisect_right(a_list, data)
#     if left_idx == right_idx:
#         print(0)
#     else:
#         print(1)

# 문제 4. 숫자 카드 2
# from bisect import bisect_left, bisect_right
#
# n = int(input())
# card_list = list(map(int, input().split()))
# card_list.sort()
#
# m = int(input())
# m_list = list(map(int, input().split()))
#
# for data in m_list:
#     left_idx = bisect_left(card_list, data)
#     right_idx = bisect_right(card_list, data)
#     print(right_idx - left_idx, end=' ')

# 문제 5. 나무 자르기
# n, m = map(int, input().split())
# tree_height = list(map(int, input().split()))
#
# start = 0
# end = max(tree_height)
# result = 0
#
# while start <= end:
#     total = 0
#     mid = (start + end) // 2
#     for height in tree_height:
#         if height > mid:
#             total += height - mid
#     if total == m:
#         result = mid
#         break
#     elif total < m:
#         end = mid - 1
#     else:
#         result = mid
#         start = mid + 1
#
# print(result)

# 문제 6. 랜선 자르기
# k, n = map(int, input().split())
# lan_list = []
#
# for _ in range(k):
#     lan_list.append(int(input()))
#
# start = 0
# end = max(lan_list)
# result = 0
#
# while start <= end:
#     mid = (start + end) // 2 if (start + end) // 2 > 0 else 1
#     total = 0
#
#     for lan in lan_list:
#         if lan >= mid:
#             total += lan // mid
#
#     if total < n:
#         end = mid - 1
#     else:
#         result = mid
#         start = mid + 1
#
# print(result)

# 문제 7. 좋다
# from bisect import bisect_left, bisect_right
# n = int(input())
# num_list = list(map(int, input().split()))
# num_list.sort()
#
# result_list = [0]*n
# for i in range(n):
#     minus_list = [x - num_list[i] for x in num_list]
#     for j in range(n):
#         if i == j:
#             continue
#         else:
#             left = bisect_left(num_list, minus_list[j])
#             right = bisect_right(num_list, minus_list[j])
#             if right - left == 2 and (left <= i < right and left <= j < right):
#                 continue
#             elif right - left == 1 and (left == i or left == j):
#                 continue
#             elif left == right or result_list[j]:
#                 continue
#             elif left < right:
#                 result_list[j] = 1
#
# print(result_list.count(1))
