unik = False
pokusy = 3
import random
tajny_kod = str(random.randint(100,999))

while pokusy > 0 and not unik:

    print("Máš", pokusy,  "pokusy")
    print("1 - Prohledat stůl")
    print("2 - zkusit otevřít dveře")
    print("3 - podívat se pod koberec\n")

    volba = input("Co uděláš?")

    if volba == "1":
        print("Našel jsi kód", tajny_kod)

    elif volba == "2":
        kód = input("Zadejte kód:")
        if kód == tajny_kod:
            unik = True
        else:
            print("Špatný kód")   
            pokusy=pokusy - 1    

    elif volba == "3":
        print("Nic tu není")
    else:
        print("Neplatná možnost")

if unik == True:
    print("Unikl jsi")
else:
    print("Prohrál jsi")