# 1이 될 때까지
n, k = map(int, input().split())

count = 0

if k == 1:
    count = n-1
else:
    while True:
        if n < k:
            count += n - 1
            break
        count += (n % k) + 1
        n //= k

print(count)