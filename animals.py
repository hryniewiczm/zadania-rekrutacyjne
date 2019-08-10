chickens_legs = 2
cows_legs = 4
pigs_legs = 4

def animals(chickens, cows, pigs):
    return (chickens * chickens_legs) + (cows * cows_legs) + (pigs * pigs_legs)

print(animals(1,2,4))