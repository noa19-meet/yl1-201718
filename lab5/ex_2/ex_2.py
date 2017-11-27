

#from turtle import Turtle 
from turtle import *
class Hexagon (Turtle):
	def __init__(self,size):
		Turtle. __init__(self)
		#self.shapesize(size)
		#self.shape("Hexagon")
		self.home()
		self.begin_poly()
		self.penup()
		for i in range(6):
			self.fd(100)
			self.right(60)
		self.end_poly()
		he = self.get_poly()
		register_shape("Hexagon",he)
		self.shape("Hexagon")

hexagon1= Hexagon(10)
mainloop()
