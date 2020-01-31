# Testing Object Oriented Programming in Python

''' Inheritance '''
class ChessPiece:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
    
    def move(self):
        print("Moved by one")

class Queen(ChessPiece):
    def move(self, x, y):
        print("Moved to " + str(x) + ", " + str(y))


que = Queen(1, 2)
pic = ChessPiece(3,2)

pic.move()
que.move(2,3)


''' Duck typing (Polymorphism basically)'''
class Animal:
    def __init__(self, anim):
        try:
            anim.make_sound()
        except:
            pass

class Dog:
    def make_sound(self):
        print("woof")

class Cat:
    def make_sound(self):
        print("meow")

class Rabbit:
    pass

c = Cat()
d = Dog()
r = Rabbit()

a = Animal(c)
b = Animal(d)
e = Animal(r)


''' Abstraction '''
class Rook(ChessPiece):
    def move(self, x, y):
        print("Moved to " + str(x) + ", " + str(y))class Piece:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
    
    def move(self, x, y):
        pass

class Rook(ChessPiece):
    def move(self, x, y):
        print("Moved horizontally to " + str(x) + ", " + str(y))

class Bishop(ChessPiece):
    def move(self, x, y):
        print("Moved diagonally to " + str(x) + ", " + str(y))


rok = Rook(1, 2)
bis = Bishop(1, 2)
pic = Piece(3,2)

bis.move(5, 6)
rok.move(2,3)