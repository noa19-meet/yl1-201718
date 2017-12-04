from turtle import *
import random
import math
colormode(255)
class Ball(Turtle):
        def __init__(self,radius,color,speed):
                Turtle.__init__(self)
                self.shape("circle")
                self.shapesize(radius)
                self.color(color)
                self.speed(speed)
                self.radius=radius

ball1 = Ball(6,"red",10)
ball2 = Ball(8,"blue",4)


def random_color(ball1,ball2):
        
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        ball1.color(r,g,b)

        if ((ball1.radius+ball2.radius) >= math.sqrt(math.pow((ball1.xcor()-ball2.xcor()),2)+math.pow((ball1.ycor()-ball2.ycor()),2))):
                ball1.color(r,g,b)
                


def check_collision (ball1,ball2):
        if ((ball1.radius+ball2.radius) >= math.sqrt(math.pow((ball1.xcor()-ball2.xcor()),2)+math.pow((ball1.ycor()-ball2.ycor()),2))):
                return True

        else:
                return False

#print(check_collision(ball1,ball2))
print(random_color(ball1,ball2))
                
