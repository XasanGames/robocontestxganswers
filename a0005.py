import sys
n, a, b, c = map(int, sys.stdin.read().split())

if a + b + c >= n:
    print("Yes")
else:
    print("No")