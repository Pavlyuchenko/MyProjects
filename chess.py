class Piece:
	"""docstring for Piece"""
	def __init__(self, value, color, xPos, yPos):
		self.value = value
		self.color = color
		self.xPos = xPos
		self.yPos = yPos
		

class Pawn(Piece):
	def __init__(self, color, xPos, yPos):
		super().__init__(1, color, xPos, yPos)


	def move(self):
		pass

pwn = Pawn(True, 1, 5)
print(pwn.value, pwn.color)