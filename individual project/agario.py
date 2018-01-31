import turtle
from turtle import Turtle
import time
import random
import math

class Ball(Turtle):
        def __init__(self,x,y,dx,dy,r,color):
                Turtle.__init__(self)
                self.x=x
                self.y=y
                self.dx=dx
                self.dy=dy
                self.penup()
                self.goto(x, y)
                self.r=r
                self.color(color,color)
                self.shape("circle")
                self.shapesize(r/10)

        def move(self,screen_width,screen_height):
                current_x = self.xcor()
                new_x=self.xcor()+self.dx
                current_y = self.ycor()
                new_y=self.ycor()+self.dy
                right_side_ball= new_x+self.r
                left_side_ball=new_x-self.r
                top_side_ball=new_y+self.r
                bottom_side_ball=new_y-self.r
                self.goto(new_x,new_y)

                if right_side_ball>screen_width:
                        self.dx=-self.dx
                        self.clear()
                elif left_side_ball<(-screen_width):
                       self.dx=-self.dx
                       self.clear()
                elif top_side_ball>screen_height:
                        self.dy=-self.dy
                        self.clear()
                elif bottom_side_ball<(-screen_height):
                        self.dy=-self.dy
                        self.clear()
                
        
turtle.hideturtle()
turtle.tracer(0)

RUNNING = True
SLEEP = 0.05
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

MY_BALL = Ball(0,0, 0, 0, 30, "red") 

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 30
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY= 5

Balls= []

for i in range (NUMBER_OF_BALLS):
        x=random.randint(-(SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
        y=random.randint(-(SCREEN_HEIGHT) + MAXIMUM_BALL_RADIUS ,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
        
        dx= random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
        while dx==0:
                dx= random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
        
        dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
        while dy==0:
                dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
        
        radius=random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
        color= (random.random(), random.random(), random.random())
        new = Ball(x,y,dx,dy,radius,color)
        Balls.append(new)


def collide(ball_a,ball_b):
        if ball_a==ball_b:
                return False
        x1=ball_a.xcor() 
        y1=ball_a.ycor()
        x2=ball_b.xcor()
        y2=ball_b.ycor()
        D = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
        if D+10<=ball_a.r+ball_b.r:
                return True
        else:
                return False

def check_all_balls_collision():
        for ball_a in Balls:
                for ball_b in Balls :
                        if collide(ball_a,ball_b):
                                r_a=ball_a.r
                                r_b=ball_b.r
                                x=random.randint(-(SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
                                y=random.randint(-(SCREEN_HEIGHT) + MAXIMUM_BALL_RADIUS ,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
                                dx= random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
                                while dx==0:
                                        dx= random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)

                                dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
                                while dy==0:
                                        dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
                                radius=random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
                                color= (random.random(), random.random(), random.random())

                                if r_a<r_b:
                                        r_b+=1
                                        ball_b.r =r_b
                                        ball_b.shapesize(r_b/10)

                                        ball_a.x=x
                                        ball_a.y=y
                                        ball_a.goto(x,y)
                                        ball_a.dx=dx
                                        ball_a.dy=dy
                                        ball_a.r=radius
                                        ball_a.color(color)
                                        ball_a.shape("circle")
                                        ball_a.shapesize(r_a/10)

                                elif r_a>r_b:
                                        r_a+=1
                                        ball_a.r=r_a
                                        ball_a.shapesize(r_a/10)

                                        ball_b.x=x
                                        ball_b.y=y
                                        ball_b.goto(x,y)
                                        ball_b.dx=dx
                                        ball_b.dy=dy
                                        ball_b.r=radius 
                                        ball_b.color(color)
                                        ball_b.shape("circle")
                                        ball_b.shapesize(r_b/10)
                        
def check_myball_collision():
        r_my=MY_BALL.r
        for i in Balls :
                collision = collide(MY_BALL,i)
                if collision:
                        r_i = i.r
                        if r_i>r_my:
                                return False
                        else:
                                x=random.randint(-(SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
                                y=random.randint(-(SCREEN_HEIGHT) + MAXIMUM_BALL_RADIUS ,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)

                                dx= random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
                                while dx==0:
                                                dx= random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)

                                dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
                                while dy==0:
                                        dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
                                radius=random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
                                color= (random.random(), random.random(), random.random())

                                i.x=x
                                i.y=y
                                i.goto(x,y)
                                i.dx=dx
                                i.dy=dy
                                i.r=radius 
                                i.color(color)
                                i.shape("circle")
                                i.shapesize(r_i/10)
                                
                                r_my+=1
                                MY_BALL.r=r_my
                                MY_BALL.shapesize(r_my/10)
        return True

def movearound(event):
        MY_BALL.goto(event.x - SCREEN_WIDTH,SCREEN_HEIGHT - event.y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while RUNNING:
        if SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2:
                SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
                SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
        for i in Balls:
                i.move(SCREEN_HEIGHT,SCREEN_WIDTH)
        check_all_balls_collision()
        RUNNING=check_myball_collision()
        turtle.getscreen().update()
        time.sleep(SLEEP)


turtle.mainloop()















                        

        
        



                                















        


































