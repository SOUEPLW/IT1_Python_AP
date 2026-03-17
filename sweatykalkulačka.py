while (True):
    cislo = int(input("Zadejte čislo "))
    cislo2 = int(input("Zadejte 2. číslo "))
    print("1. součet \n2. součin \n3. rozdíl \n4- podíl")
    operace = int(input ("Vyberte číslo operace, kterou chcete požít "))
    match operace:
        case 1: 
            soucet = cislo + cislo2
            print(soucet)
        case 2: 
            rozdil = cislo - cislo2
            print(rozdil)
        case 3: 
            soucin = cislo * cislo2
            print(soucin)
        case 4: 
            if cislo2 == 0:
                print("Nelze dělit 0")
            else:
                podil = cislo / cislo2
    print(podil)
    konec = input("Přejete si ukončit program? Y/N ")
    if konec.lower() == "y":
        break