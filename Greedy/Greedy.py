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
n = int(input())
count = 0
div_5 = n // 5
remain_5 = n % 5
div_3 = 0
remain_3 = 0
result = 0

if remain_5 == 0:
    result = div_5
else:
    while True:
        div_3 = remain_5 // 3
        remain_3 = remain_5 % 3
        if remain_3 == 0:
            result = div_5 + div_3
            break
        else:
            if div_5 > 0:
                div_5 -= 1
                remain_5 += 5
                n -= 5
            else:
                result = -1
                break

print(result)
