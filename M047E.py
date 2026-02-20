def solve():
    import sys
    # Читаем число из ввода
    line = sys.stdin.read().strip()
    if not line: return
    n = int(line)

    if n == 0:
        print("nol")
        return

    # Словари
    b = {1:"bir", 2:"ikki", 3:"uch", 4:"to'rt", 5:"besh", 6:"olti", 7:"yetti", 8:"sakkiz", 9:"to'qqiz"}
    o = {1:"o'n", 2:"yigirma", 3:"o'ttiz", 4:"qirq", 5:"ellik", 6:"oltmish", 7:"yetmish", 8:"sakson", 9:"to'qson"}

    res = []

    # Тысячи
    if n >= 1000:
        res.append(b[n // 1000] + " ming")
        n %= 1000
    
    # Сотни
    if n >= 100:
        res.append(b[n // 100] + " yuz")
        n %= 100

    # Десятки
    if n >= 10:
        res.append(o[n // 10])
        n %= 10

    # Единицы
    if n > 0:
        res.append(b[n])

    print(" ".join(res))

solve()