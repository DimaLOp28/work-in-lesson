cisla = [3, 98, 49, 23, 42, 8, 52, 69]
hodnota = int(input("Zadej číslo, které chceš najít v poli: "))
nalezeno = False
for i in range(len(cisla)):
    if cisla[i] == hodnota:
        print(f"Našel jsem tuto hodnotu na pozici {i}!")
        nalezeno = True
        break
    if not nalezeno:
        print("Zadaná hodnota tady není.")
