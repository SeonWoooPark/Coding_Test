# 문제 1. 최대 상금
# import sys
# sys.setrecursionlimit(10**8)
# max_list = []
# T = int(input())
# for test_case in range(1, T + 1):
#     num, n = input().split()
#     count = int(n)
#     array = list(map(int, num))
#     sorted_arr = sorted(array, reverse=True)
#     sorted_str = [str(x) for x in sorted_arr]
#     sorted_num = int(''.join(sorted_str))
#     set_num = set()
#     isFirst = True
#
#     def dfs(array, count, set_num):
#         global sorted_num
#         n = len(array)
#         if count == 0:
#             return max(set_num)
#
#         arr_str = [str(x) for x in array]
#         arr_num = int(''.join(arr_str))
#         set_num.add(arr_num)
#
#         if arr_num == sorted_num:
#             if count % 2 == 0:
#                 return arr_num
#             else:
#                 same_value = False
#                 for data in array:
#                     if array.count(data) > 1:
#                         same_value = True
#                         break
#
#                 if same_value:
#                     return arr_num
#
#                 arr_str[n-2], arr_str[n-1] = arr_str[n-1], arr_str[n-2]
#                 arr_num = int(''.join(arr_str))
#                 sorted_num = arr_num
#                 return arr_num
#
#
#         count -= 1
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 arr_copy = array[:]
#                 arr_copy[i], arr_copy[j] = arr_copy[j], arr_copy[i]
#                 copy_str = [str(x) for x in arr_copy]
#                 copy_num = int(''.join(copy_str))
#                 set_num.add(copy_num)
#                 dfs_num = dfs(arr_copy, count, set_num)
#                 if dfs_num == sorted_num:
#                     return dfs_num
#                 set_num.add(dfs_num)
#
#         return max(set_num)
#
#
#     max_value = dfs(array, count, set_num)
#     max_list.append(max_value)
#
# for i in range(T):
#     print(f'#{i+1} {max_list[i]}')

# 문제 2. 최빈수 구하기
# T = int(input())
# result_list = []
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     input()
#     grade_list = list(map(int, input().split()))
#     grade_num = [0] * 101
#
#     for grade in grade_list:
#         grade_num[grade] += 1
#
#     max_count = max(grade_num)
#     result = []
#     for i in range(len(grade_num)):
#         if grade_num[i] == max_count:
#             result.append(i)
#
#     result_list.append(max(result))
#
# for i in range(1, T+1):
#     print(f'#{i} {result_list[i-1]}')

# 문제 3.Flatten
import heapq
result_list = []

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    dump = int(input())
    max_heap = []
    min_heap = []
    height_list = list(map(int, input().split()))
    isMaxDump = False

    for height in height_list:
        heapq.heappush(min_heap, height)
        heapq.heappush(max_heap, -height)

    for _ in range(dump):
        max_height = -heapq.heappop(max_heap)
        min_height = heapq.heappop(min_heap)
        if (max_height - min_height) <= 1:
            result_list.append(max_height-min_height)
            isMaxDump = True
            break
        max_height -= 1
        min_height += 1
        heapq.heappush(max_heap, -max_height)
        heapq.heappush(min_heap, min_height)

    if not isMaxDump:
        max_height = -heapq.heappop(max_heap)
        min_height = heapq.heappop(min_heap)
        result_list.append(max_height - min_height)

for i in range(1, T+1):
    print(f'#{i} {result_list[i-1]}')

# a = []
# b = []
# for i in range(10):
#     heapq.heappush(a, i)
#     heapq.heappush(b, -i)
#
# for j in range(100):
#     b_max = -heapq.heappop(b)
#     a_min = heapq.heappop(a)
#     if (b_max - a_min) <= 1:
#         heapq.heappush(a, a_min)
#         heapq.heappush(b, -b_max)
#         break
#     b_max -= 1
#     a_min += 1
#     heapq.heappush(a, a_min)
#     heapq.heappush(b, -b_max)
#
# for i in range(len(a)):
#     print(heapq.heappop(a), end=' ')
# print()
# for i in range(len(b)):
#     print(-heapq.heappop(b), end=' ')
# print(b)