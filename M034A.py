import sys

# Читаем абсолютно все числа из ввода
data = sys.stdin.read().split()
if data:
    n = int(data[0])  # Первое число — это количество тестов
    idx = 1
    
    for _ in range(n):
        # Берем следующие три числа для каждого теста
        b = int(data[idx])
        k = int(data[idx+1])
        shs = int(data[idx+2])
        idx += 3
        
        # Проверка условий (регистр важен: "Yes" и "No")
        if (200 <= b <= 300) and (k >= 50) and (shs >= 150):
            print("Yes")
        else:
            print("No")