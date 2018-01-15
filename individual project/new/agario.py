import turtle
import time
import random
import Ball
import Math

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
	def turtle.tracer(0)
	

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
	
self.hideturtle()

boolean RUNNING = True
float SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

MY_BALL = Ball()

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS to = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY= 5

Balls= [new]

for i in range (NUMBER_OF_BALLS):

	x=random.randint(-(SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y=random.randint(-(SCREEN_HEIGHT) + MAXIMUM_BALL_RADIUS ,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)

	dx= random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
		while (dx==0):
			dx= random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)

	dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
		while (dy==0):
			dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	radius=random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color= (random.random(), random.random(), random.random())

new = Ball(x,y,dx,dy,r,color,shape,shapesize)

Balls.append(new)

for i in (Balls) :
	i.move(SCREEN_HEIGHT,SCREEN_WIDTH)

def collide(ball_a,ball_b):
	if (ball_a==ball_b):
		return False
ball_a.xcor() = x1
ball_a.ycor() = y1
ball_b.xcor() = x2
ball_b.xcor() = y2

D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))

	


































