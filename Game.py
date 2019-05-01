import time

class Game:
	
	def __init__(self, canvas):
		self.canvas = canvas
		self.width = self.canvas.winfo_width()
		self.height = self.canvas.winfo_height()
		self.lines = []
		self.drawGrid()
		self.naughtsTurn = True
		self.gameState = []
		self.xs = []
		self.os = []
		for i in range(3):
			self.gameState.append([-1, -1, -1])
		self.canvas.bind_all("<Button-1>", self.clickEvent)
	
	
	def handleEvent(self, pos):
		if(self.gameState[pos[0]][pos[1]] == -1):
			if(self.naughtsTurn):
				self.naughtsTurn = False
				self.drawNaught(pos)
				self.gameState[pos[0]][pos[1]] = 1
			else:
				self.naughtsTurn = True
				self.drawCircle(pos)
				self.gameState[pos[0]][pos[1]] = 2
		if(self.checkWin()):
			time.sleep(1)
			if(self.naughtsTurn):
				winner = "O wins."
				win_color = "blue"
			else:
				winner = "X wins."
				win_color = "red"
			self.destroy_all()
			id = self.canvas.create_text(self.width/2, self.height/2, text=winner, fill=win_color, font=("Consolas", 18))
			self.canvas.update()
			time.sleep(2)
			self.canvas.delete(id)
			self.reset()
		if(self.isFull() and not self.checkWin()):
			time.sleep(1)
			self.destroy_all()
			id = self.canvas.create_text(self.width/2, self.height/2, text="Draw!", fill="white", font=("Consolas", 18))
			self.canvas.update()
			time.sleep(2)
			self.canvas.delete(id)
			self.reset()
	
		
	def checkWin(self):
		if(self.gameState[0][0] != -1 and self.gameState[0][0] == self.gameState[0][1] and self.gameState[0][1] == self.gameState[0][2]):
			return True
		elif(self.gameState[1][0] != -1 and self.gameState[1][0] == self.gameState[1][1] and self.gameState[1][1] == self.gameState[1][2]):
			return True
		elif(self.gameState[2][0] != -1 and self.gameState[2][0] == self.gameState[2][1] and self.gameState[2][1] == self.gameState[2][2]):
			return True
		elif(self.gameState[0][0] != -1 and self.gameState[0][0] == self.gameState[1][0] and self.gameState[1][0] == self.gameState[2][0]):
			return True
		elif(self.gameState[0][1] != -1 and self.gameState[0][1] == self.gameState[1][1] and self.gameState[1][1] == self.gameState[2][1]):
			return True
		elif(self.gameState[0][2] != -1 and self.gameState[0][2] == self.gameState[1][2] and self.gameState[1][2] == self.gameState[2][2]):
			return True
		elif(self.gameState[0][0] != -1 and self.gameState[0][0] == self.gameState[1][1] and self.gameState[1][1] == self.gameState[2][2]):
			return True
		elif(self.gameState[0][2] != -1 and self.gameState[0][2] == self.gameState[1][1] and self.gameState[1][1] == self.gameState[2][0]):
			return True
		return False
		
	def isFull(self):
		for i in self.gameState:
			for j in i:
				if(j == -1):
					return False
		return True	
	
	def clickEvent(self, event):
		x = int(event.x)
		y = int(event.y)
		if(x > 0 and x < int(self.width/3)):
			m = 0
		elif(x > int(self.width/3) and x < int(2*self.width/3)):
			m = 1
		elif(x < int(self.width)):
			m = 2
		
		if(y > 0 and y < int(self.height/3)):
			n = 0
		elif(y > int(self.height/3) and y < int(2*self.height/3)):
			n = 1
		elif(y < int(self.height)):
			n = 2
		
		self.handleEvent([m, n])
		
	def drawCircle(self, pos):
		offset = 30
		lineWidth = 10
		x = int(pos[0]*(self.width/3))
		y = int(pos[1]*(self.height/3))
		a = self.canvas.create_oval(x+offset, y+offset, (x+int(self.width/3)-offset), (y+int(self.height/3)-offset), fill='blue')
		b = self.canvas.create_oval(x+offset+lineWidth, y+offset+lineWidth, (x+int(self.width/3)-offset)-lineWidth, (y+int(self.height/3)-offset)-lineWidth, fill='black')
		self.os.append([a, b])
		self.canvas.update()
	
	def drawNaught(self, pos):
		offset = 40
		lineWidth = 10
		x = int(pos[0]*(self.width/3))
		y = int(pos[1]*(self.height/3))
		a = self.canvas.create_line(x+offset, y+offset, (x+int(self.width/3)-offset), (y+int(self.height/3)-offset), fill='red', width=lineWidth)
		b = self.canvas.create_line(x+(int(self.width/3))-offset, y+offset, x+offset, y+(int(self.height/3))-offset, fill='red', width=lineWidth)
		self.xs.append([a, b])
		self.canvas.update()
	
	def drawGrid(self):
		for i in list(range(0, self.width, int(self.width/3))):
			x = self.canvas.create_line(i, 0, i, self.height, fill='white')
			self.lines.append(x)
		for i in list(range(0, self.height, int(self.height/3))):
			y = self.canvas.create_line(0, i, self.width, i, fill='white')
			self.lines.append(y)
		
	def destroy_all(self):
		for i in self.lines:
			self.canvas.delete(i)
		for i in self.xs:
			for j in i:
				self.canvas.delete(j)
		for i in self.os:
			for j in i:
				self.canvas.delete(j)
		self.canvas.update()
	
	def reset(self):
		self.lines = []
		self.drawGrid()
		self.naughtsTurn = True
		self.gameState = []
		self.xs = []
		self.os = []
		for i in range(3):
			self.gameState.append([-1, -1, -1])
		self.canvas.update()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
