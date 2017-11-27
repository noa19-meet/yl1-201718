from turtle import *
class Polygon (Turtle):
	def __init__(self,lines):
		Turtle. __init(self)
		self.home()
		self.begin_poly()
		self.penup()
		for i in range(360 / lines):
				self.fd(100)
				self.right(60)
		self.end_poly()
		Polygon = self.get_poly()
		register_shape("Polygon",Polygon1)
		self.shape("Polygon")
Polygon1=Polygon(4)
mainloop()
		








