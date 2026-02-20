import sys

# Считываем всё сразу: первое число будет N, остальные — элементами массива
data = sys.stdin.read().split()

if data:
    # Пропускаем первое число (N), берем только сам набор чисел
    numbers = data[1:] 
    
    res = 0
    for x in numbers:
        res ^= int(x) # XOR убирает все пары и оставляет одиночку
    
    print(res)