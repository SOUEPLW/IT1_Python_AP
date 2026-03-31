import random
hodu = 0
while True:
    num = int(input("Zadejte číslo mezi 1 - 6 "))
    if 0 < num < 7:
        break


while True:
    hodu += 1
    rand = random.randint(1, 6)
    rand2 = random.randint(1, 6)
    print(rand, rand2)
    
    if rand == rand2 == num:
        break
        print("Hodů bylo ", hodu)
