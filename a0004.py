numbers = input("Введте массив : ").split()
res = 0

for x in numbers:
    res ^= int(x)

print(res)