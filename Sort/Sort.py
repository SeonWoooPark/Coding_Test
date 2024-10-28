# 문제 1. 두 배열의 원소 교체
# n, k = map(int, input().split())
#
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
#
# a.sort()
# b.sort(reverse=True)
#
# for i in range(k):
#     if a[i] < b[i]:
#         a[i], b[i] = b[i], a[i]
#     else:
#         break
#
# print(sum(a))

# 문제 2. 수 정렬하기 (백준 Sort 유형)
# import sys
# sys.setrecursionlimit(100000)
#
# def input():
#     return sys.stdin.readline().rstrip()
#
# n = int(input())
# input_list = []
# for _ in range(n):
#     input_list.append(int(input()))
#
# # 정석 quick sort
# def f_quick_sort(array, start, end):
#     if start >= end:
#         return
#
#     pivot = start
#     left = start+1
#     right = end
#
#     while left <= right:
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
#         if left > right:
#             array[pivot], array[right] = array[right], array[pivot]
#         else:
#             array[left], array[right] = array[right], array[left]
#
#     f_quick_sort(array, start, right-1)
#     f_quick_sort(array, right+1, end)
#
#
# # # python의 장점을 이용한 quick sort
# # def s_quick_sort(array):
# #     if len(array) <= 1:
# #         return array
# #
# #     pivot = array[0]
# #     tail = array[1:]
# #     left_side = [x for x in tail if x <= pivot]
# #     right_side = [ x for x in tail if x > pivot]
# #
# #     return s_quick_sort(left_side) + [pivot] + s_quick_sort(right_side)
# #
# f_quick_sort(input_list, 0, len(input_list)-1)
#
# # sorted_list = s_quick_sort(input_list)
#
# for data in input_list:
#     sys.stdout.write(str(data) + '\n')


# 문제 3. 수 정렬하기 2
# import sys
# sys.setrecursionlimit(100000)
#
# def input():
#     return sys.stdin.readline().rstrip()
#
# n = int(input())
# input_list = []
# for _ in range(n):
#     input_list.append(int(input()))
#
# input_list.sort()
#
# for data in input_list:
#     sys.stdout.write(str(data) + '\n')

# 문제 4. 단어 정렬
# n = int(input())
# word_list = []
# for _ in range(n):
#     word_list.append(input())
#
# word_list = list(set(word_list))
# sorted_word = sorted(word_list, key=lambda x:(len(x), x))
#
# for word in sorted_word:
#     print(word)

# 문제 5. 수 찾기
from bisect import bisect_left, bisect_right

n = int(input())
find_list = list(map(int, input().split()))
find_list.sort()

m = int(input())
find_num = list(map(int, input().split()))

for num in find_num:
    find_left_index = bisect_left(find_list, num)
    if find_left_index < n and find_list[find_left_index] == num:
        print(1)
    else:
        print(0)
