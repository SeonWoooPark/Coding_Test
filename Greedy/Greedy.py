# 문제 1. 1이 될 때까지
# n, k = map(int, input().split())
#
# count = 0
#
# if k == 1:
#     count = n-1
# else:
#     while True:
#         if n < k:
#             count += n - 1
#             break
#         count += (n % k) + 1
#         n //= k
#
# print(count)

# 문제 2. 곱하기 혹은 더하기
# input_num = list(map(int,list(input())))
# result = input_num[0]
# for i in range(1, len(input_num)):
#     if result > 1 and input_num[i] > 1:
#         result *= input_num[i]
#     else:
#         result += input_num[i]
#
# print(result)

# 문제 3. 모험가 길드
# n = int(input())
# input_ = list(map(int, input().split()))
#
# input_.sort()
# count = 0
# m_count = 0
# g_fear = 0
#
# for i in range(n):
#     m_count += 1
#     if input_[i] == m_count:
#         count += 1
#         m_count = 0
#
# print(count)

# 문제 4. 설탕 배달(백준 그리디 유형)
# n = int(input())
# count = 0
# div_5 = n // 5
# remain_5 = n % 5
# div_3 = 0
# remain_3 = 0
# result = 0
#
# if remain_5 == 0:
#     result = div_5
# else:
#     while True:
#         div_3 = remain_5 // 3
#         remain_3 = remain_5 % 3
#         if remain_3 == 0:
#             result = div_5 + div_3
#             break
#         else:
#             if div_5 > 0:
#                 div_5 -= 1
#                 remain_5 += 5
#                 n -= 5
#             else:
#                 result = -1
#                 break
#
# print(result)

# 문제 5. ATM(백준 그리디 유형)
# n = int(input())
# input_p = list(map(int, input().split()))
# input_p.sort()
# result = 0
#
# for i in range(n):
#     for j in range(n-i):
#         result += input_p[j]
#
# print(result)

# 문제 6. 동전 0(백준 그리디 유형)
# n, k = map(int, input().split())
# input_coin = []
# count = 0
# idx = n-1
#
# for i in range(n):
#     input_coin.append(int(input()))
#
# while k > 0:
#     count += (k // input_coin[idx])
#     k = k % input_coin[idx]
#     idx -= 1
#
# print(count)

# 문제 7. 회의실 배정(백준 그리디 유형)
# n = int(input())
# input_meeting = []
# result_meeting = []
#
# for i in range(n):
#     meeting_tup = tuple(map(int, input().split()))
#     input_meeting.append(meeting_tup)
#
# input_meeting.sort()
# own = input_meeting[0]
#
# for i in range(len(input_meeting)):
#     if i == 0:
#         continue
#     if own[1] <= input_meeting[i][0]:
#         result_meeting.append(own)
#         own = input_meeting[i]
#         continue
#     elif own[1] > input_meeting[i][1]:
#         own = input_meeting[i]
#
# if len(result_meeting) == 0:
#     result_meeting.append(own)
# elif own[0] >= result_meeting[len(result_meeting)-1][1]:
#     result_meeting.append(own)
#
# print(len(result_meeting))

# 문제 8. 잃어버린 괄호(백준 그리디 유형)
# input_equal = list(input())
# input_str = ""
# plus_count = 0
# is_opened = False
# num_idx = 0
# for i in range(len(input_equal)):
#     if input_equal[i] != '+' and input_equal[i] != '-':
#         continue
#     else:
#         input_str += str(int("".join(input_equal[num_idx:i])))
#         num_idx = i + 1
#         if input_equal[i] == '-' and not is_opened:
#             input_str += '-('
#             is_opened = True
#         elif input_equal[i] == '-' and is_opened:
#             input_str += ')-('
#         elif input_equal[i] == '+':
#             input_str += '+'
#
# input_str += str(int("".join(input_equal[num_idx:])))
# if is_opened:
#     input_str += ')'
#
# print(eval(input_str))

# 문제 9. 보물(백준 그리디 유형)
# n = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# result = 0
#
# for _ in range(n):
#     min_a = a.pop(a.index(min(a)))
#     max_b = b.pop(b.index(max(b)))
#     result += min_a * max_b
#
# print(result)

# 문제 10. 보석 도둑(백준 그리디 유형)
# import heapq
#
# n, k = map(int, input().split())
# jewel_list = []
# bag_list = []
# result = 0
#
# for _ in range(n):
#     jewel_tup = list(map(int, input().split()))
#     jewel_list.append(jewel_tup)
#
# for _ in range(k):
#     bag_list.append(int(input()))
#
# bag_list.sort()
# jewel_list.sort()
# heap = []
#
# for bag in bag_list:
#     while jewel_list and jewel_list[0][0] <= bag:
#         heapq.heappush(heap, -jewel_list[0][1])
#         heapq.heappop(jewel_list)
#     if heap:
#         result -= heapq.heappop(heap)
#
# print(result)
