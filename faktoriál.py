fakt = int(input("Zadejte číslo, jehož faktoriál chcete "))
vysledek = 1
for i in range(1, fakt+1):
    vysledek *= i
    print(vysledek)