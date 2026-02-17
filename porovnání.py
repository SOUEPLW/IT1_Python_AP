x = int (input ("Zadejte první číslo: "))
y = int (input ("Zadejte druhé číslo: "))
if x > y:
    #print(x + "je větší než " + y) nefunkční kvůli datovému typu
    #print(x, "je větší než " ,y)
    #print (str(x) + "je větší než " + str(y)) přetypování z integer na string
    #print(f"{x} + je větší než  + {y}") složené závorky = right alt + B/N
    print(f"{x} je větší než {y}")

elif x == y:
    print("Zadaná čísla jsou stejná")

else:
    print(f"{y} je větší než {x}")
