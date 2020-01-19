from tkinter import *
import string

class Board(object):
    """docstring for Board"""
    def __init__(self, player=True):
        self.playboard = self.create_board()
        self.values, self.pieces = self.create_pieces()

    def create_board(self):
        playboard = [["-"] * 8, ["-"] * 8, ["-"] * 8, ["-"] * 8, ["-"] * 8, ["-"] * 8, ["-"] * 8, ["-"] * 8]
        '''
        for letter in letters:
            for number in numbers:
                playboard[counter][number] = str(letter) + str(number+1)

            counter += 1'''
        playboard = playboard[::-1]
        return playboard

    def create_pieces(self):
        white = [Pawn(True, 6, 0), Pawn(True, 6, 1), Pawn(True, 6, 2), Pawn(True, 6, 3), Pawn(True, 6, 4), Pawn(True, 6, 5), Pawn(True, 6, 6), Pawn(True, 6, 7),
                Rook(True, 7, 0), Knight(True, 7, 1), Bishop(True, 7, 2), Queen(True, 7, 3), King(True, 7, 4), Bishop(True, 7, 5), Knight(True, 7, 6), Rook(True, 7, 7)]

        black = [Pawn(True, 1, 0), Pawn(True, 1, 1), Pawn(True, 1, 2), Pawn(True, 1, 3), Pawn(True, 1, 4), Pawn(True, 1, 5), Pawn(True, 1, 6), Pawn(True, 1, 7),
                Rook(True, 0, 0), Knight(True, 0, 1), Bishop(True, 0, 2), Queen(True, 0, 3), King(True, 0, 4), Bishop(True, 0, 5), Knight(True, 0, 6), Rook(True, 0, 7)]

        white_value = 0
        black_value = 0

        for i, j in zip(white, black):
            self.playboard[i.xPos][i.yPos] = i
            white_value += i.value

            self.playboard[j.xPos][j.yPos] = j
            black_value += j.value

        values = [white_value, black_value]
        pieces = [white, black]

        return values, pieces

    def print_board(self):
        ascii_counter = 0

        print("    1   2   3   4   5   6   7   8")
        print("  ---------------------------------")
        for x in self.playboard:
            print(chr(ascii_counter+97), "", end="")
            for y in x:
                print("|", y, "", end="")
            print("|", end="")
            print("", chr(ascii_counter+97))
            ascii_counter += 1
            if ascii_counter != 8:
                print("  |---+---+---+---+---+---+---+---|")
        print("  ---------------------------------")
        print("    1   2   3   4   5   6   7   8")

    def move(self, old_loc, new_loc):
        piece = self.playboard[int(old_loc[0])][int(old_loc[1])-1]

        self.playboard[int(old_loc[0])][int(old_loc[1])-1] = "-"
        self.playboard[int(new_loc[0])][int(new_loc[1])-1] = piece

        self.print_board()


class Piece:
    """docstring for Piece"""
    def __init__(self, value, player, xPos, yPos, img):
        self.value = value
        self.player = player
        self.xPos = xPos
        self.yPos = yPos
        self.img = img

    def __str__(self):
        return self.img


class Pawn(Piece):
	def __init__(self, player, xPos, yPos):
		super().__init__(1, player, xPos, yPos, "P")

	def move(self):
		self.yPos += 1


class Rook(Piece):
    def __init__(self, player, xPos, yPos):
        super().__init__(5, player, xPos, yPos, "R")


class Knight(Piece):
    def __init__(self, player, xPos, yPos):
        super().__init__(3, player, xPos, yPos, "N")


class Bishop(Piece):
    def __init__(self, player, xPos, yPos):
        super().__init__(3, player, xPos, yPos, "B")


class King(Piece):
    def __init__(self, player, xPos, yPos):
        super().__init__(0, player, xPos, yPos, "K")


class Queen(Piece):
    def __init__(self, player, xPos, yPos):
        super().__init__(10, player, xPos, yPos, "Q")


brd = Board()
brd.print_board()
print(brd.values)

moves = ["g5 e5", "h4 d8", "g4 e4", "h3 e6", "h2 f3", "f3 d2", ]

counter = 0

for move in moves:
    piece_to_play = move.split(" ")[0]
    piece_new_location = move.split(" ")[1]

    piece_to_play = str(ord(piece_to_play[0])-97) + piece_to_play[1]
    piece_new_location = str(ord(piece_new_location[0])-97) + piece_new_location[1]

    brd.move(piece_to_play, piece_new_location)



'''root = Tk()

topFrame = Frame(root)
topFrame.pack()
btn = Button(topFrame, text="start", fg="red")
btn.pack()

root.mainloop()
'''
