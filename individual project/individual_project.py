from turtle import *
import math
class Ball (Turtle):
	def __init__(self,x,y,dx,dy,r,color,shape,shapesize):
		self.x(x)
		self.y(y)
		self.dx(dx)
		self.dy(dy)
		self.r(r)
		self.color(color)
		self.shape("circle")
		self.shapesize(r/10)
		self.penup()

	def move(self,screen_width,screen_height):
		current_x = self.xcor()
		new_x=self.xcor()+self.dx
		current_y = self.ycor()
		nex_y=self.ycor()+self.dy
		right_side_ball= new_x+r
		left_side_ball=new_x-r
		top_side_ball=new_y+r
		bottom_side_ball=new_y-r
                self.goto(new_x,new_y)



		






