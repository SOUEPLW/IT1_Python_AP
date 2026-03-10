max = -1
for i in range(-10, 10):
    cislo = int(input("Zadejte číslo "))
    if cislo > max:
        max = cislo
print("Maximální zadané číslo bylo", max)