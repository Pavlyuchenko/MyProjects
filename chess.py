from tkinter import *
import string

class Board(object):
    """docstring for Board"""
    def __init__(self, player=True):
        letters = list(string.ascii_lowercase)[0:8]
        numbers = list(x+1 for x in range(0, 8))
        playboard = [""] * 8

        for letter, number in zip(letters, numbers):
            playboard[number].append(str(letter) + str(number))

class Piece:
    """docstring for Piece"""
    def __init__(self, value, player, xPos, yPos):
        self.value = value
        self.player = player
        self.xPos = xPos
        self.yPos = yPos


class Pawn(Piece):
	def __init__(self, player, xPos, yPos):
		super().__init__(1, player, xPos, yPos)


	def move(self):
		pass

pwn = Pawn(True, 1, 5)
print(pwn.value, pwn.player)

letters = list(string.ascii_lowercase)[0:8]
numbers = list(x for x in range(0, 8))
playboard = [
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
            ]
counter = 0

for letter in letters:
    for number in numbers:
        playboard[counter][number] = str(letter) + str(number+1)

    counter += 1

print(playboard)
'''root = Tk()

topFrame = Frame(root)
topFrame.pack()
btn = Button(topFrame, text="start", fg="red")
btn.pack()

root.mainloop()
'''
