from tkinter import *
from Game import *
import time

def run():
	
	root = Tk()
	root.title("Tic Tac Toe")
	root.geometry("+500+150")
	canvas = Canvas(root, width=400, height=400, bg='black', bd=0, highlightthickness=0)
	canvas.pack()
	root.update_idletasks()
	game = Game(canvas)
	root.mainloop()

if __name__ == '__main__':
	run()
	

