yil = int(input("Введите год : ").strip())

oy_kunlari = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Найти высоковный год
if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
    oy_kunlari[1] = 29  # Февраль 28-ое

kun_soni = 356
oy = 1

while kun_soni > oy_kunlari[oy - 1]:
    kun_soni -= oy_kunlari[oy - 1]
    oy += 1

dd = f"{kun_soni:02d}"
mm = f"{oy:02d}"
yyyy = f"{yil:04d}"

print(f"{dd}/{mm}/{yyyy}")