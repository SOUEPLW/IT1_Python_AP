import random
cards = list(range(1, 33))
shuffled = []
krok = 0
print(cards)
for _ in range(len(cards)):
    while True:
        card = random.randint(0,31)
        krok += 1
        if cards[card] != None:
            shuffled.append(cards[card])
            cards[card] = None
            break
print(shuffled)
print("Kroků bylo", krok)
