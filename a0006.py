def solve():
    try:
        line = input().split()
        if not line: return
        n = int(line[0])
    except EOFError:
        return

    if n < 2:
        print("Bobur")
        return

    # Решето Эратосфена
    primes = [True] * (n + 1)
    count = 0
    for p in range(2, n + 1):
        if primes[p]:
            count += 1
            # Вычеркиваем кратные
            for i in range(p * p, n + 1, p):
                primes[i] = False
    
    if count % 2 == 1:
        print("Ali")
    else:
        print("Bobur")

solve()