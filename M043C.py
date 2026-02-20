line = input().strip()
t = int(line)
for _ in range(t):
    n = int(input().strip())
    a = list(map(int,input().split()))
    if len(set(a)) == n:
        print("Yes")
    else:
        print("No")