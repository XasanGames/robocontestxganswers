n = int(input())
if n >= 1:
    res = n * (n + 1) // 2
else:
    res = (1 + n) * (abs(n - 1) + 1) // 2