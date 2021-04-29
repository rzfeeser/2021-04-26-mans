#!/usr/bin/python3
"""building a script with a class and methods"""

class Player:
    def __init__(self, name, numlives):
        self.name = name
        self.numlives = numlives
    
    def livesincrease(self, amount):
        self.numlives += amount

    def livesdecrease(self, amount):
        self.numlives = self.numlives - amount


def zach():
    print("call this anytime, anywhere")


p1 = Player("mario", 3)
p2 = Player("luigi", 3)

# what are p1 and p2
print(p1)
print(p2)

# what are the NAMES inside of p1 and p2?
print(dir(p1))

print(dir(p2))

# display the attributes avail in p1
print(p1.numlives)
print(p1.name)

# use a METHOD to change our object
p1.livesincrease(3)
print(p1.numlives)



zach()

zach()
