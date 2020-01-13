import random
import time

class Bear:
    def __init__(self):
        self.posX = random.randint(0, base_x)
        self.posY = random.randint(0, base_y)

        while True:
            if river[self.posY][self.posX] != "B" and river[self.posY-1][self.posX] != "B" and river[self.posY+1][self.posX] != "B" and river[self.posY][self.posX-1] != "B" and river[self.posY][self.posX+1] != "B" and river[self.posY][self.posX] != "F" and river[self.posY-1][self.posX] != "F" and river[self.posY+1][self.posX] != "F" and river[self.posY][self.posX-1] != "F" and river[self.posY][self.posX+1] != "F":
                river[self.posY][self.posX] = "B"
                break
            self.posX = random.randint(0, base_x)
            self.posY = random.randint(0, base_y)


    def update(self, rand):
        river[self.posY][self.posX] = basic_sign

        if rand == 1: #Go left
            if self.posX == 0:
                self.posX += 1
            else:
                self.posX -= 1
        elif rand == 2: #Go right
            if self.posX == base_x+1:
                self.posX -= 1
            else:
                self.posX += 1
        elif rand == 3: #Go top
            if self.posY == 0:
                self.posY += 1
            else:
                self.posY -= 1
        elif rand == 4: #Go bot
            if self.posY == base_y+1:
                self.posY -= 1
            else:
                self.posY += 1

        if river[self.posY][self.posX] == "B":
            bears.append(Bear())
            print("NEW BEAR!!! on location", self.posX, self.posY)
            return

        river[self.posY][self.posX] = "B"

class Fish:
    def __init__(self):
        self.posX = random.randint(0, base_x)
        self.posY = random.randint(0, base_y)

        while True:
            if river[self.posY][self.posX] != "B" and river[self.posY-1][self.posX] != "B" and river[self.posY+1][self.posX] != "B" and river[self.posY][self.posX-1] != "B" and river[self.posY][self.posX+1] != "B" and river[self.posY][self.posX] != "F" and river[self.posY-1][self.posX] != "F" and river[self.posY+1][self.posX] != "F" and river[self.posY][self.posX-1] != "F" and river[self.posY][self.posX+1] != "F":
                river[self.posY][self.posX] = "F"
                break
            self.posX = random.randint(0, base_x)
            self.posY = random.randint(0, base_y)


    def __del__(self):
        self.posX = None
        self.posY = None
    

    def update(self, rand):
        river[self.posY][self.posX] = basic_sign

        old_x = self.posX
        old_y = self.posY

        if rand == 1: #Go left
            if self.posX == 0:
                #river[self.posY][self.posX] = ">"
                self.posX +=1
            else:
                #river[self.posY][self.posX] = "<"
                self.posX -= 1
        elif rand == 2: #Go right
            if self.posX == base_x+1:
                self.posX -=1
            else:
                self.posX += 1
        elif rand == 3: #Go top
            if self.posY == 0:
                self.posY +=1
            else:
                self.posY -= 1
        elif rand == 4: #Go bot
            if self.posY == base_y+1:
                self.posY -=1
            else:
                self.posY += 1

        if river[self.posY][self.posX] == "F":
            fishes.append(Fish())
            print("Fishes had sex on location", self.posX, self.posY)
            return
        elif river[self.posY][self.posX] == "B":
            river[old_y][old_x] = basic_sign
            print("FISH EATEN!!! on location", old_x+1, old_y)
            fishes.remove(self)
            del self
            return

        river[self.posY][self.posX] = "F"



def print_river():
    for i in range(0, base_x+3):
        print(str(i) + " ", end="")
    for number, line in enumerate(river):
        print()
        print(str(number), "", end="")
        for x in line:
            print(str(x) + " ", end="")

    print()


def clear_screen():
    print("\n" * 10)


def new_fish(arr):
    for i in range(fish_spawn_count):
        arr.append(Fish())
    return arr


def new_bear(arr):
    for i in range(bear_spawn_count):
        arr.append(Bear())
    return arr


def update_board():
    for bear in bears:
        rand = random.randint(1, 4)
        bear.update(rand)

    for fish in fishes:
        rand = random.randint(1, 4)
        fish.update(rand)
    print_river()
    time.sleep(.5)


basic_sign = "-"
base_x = 8
base_y = 5
fish_spawn_count = 1
bear_spawn_count = 10

river = [[basic_sign]*10, [basic_sign]*10, [basic_sign]*10, [basic_sign]*10, [basic_sign]*10, [basic_sign]*10, [basic_sign]*10]

bears = []
bears = new_bear(bears)

fishes = []
fishes = new_fish(fishes)

print_river()

update_board()
update_board()
update_board()
update_board()
update_board()
update_board()
update_board()

while not fishes == []:
    update_board()

print("BEARS HAVE CONQUERED THE BOARD!!!") 

