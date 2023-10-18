import turtle
import random
sea=turtle.Screen()
sea.bgpic("back.gif")
sea.addshape("left.gif")
sea.addshape("right.gif")
sea.addshape("coin.gif")



hunter=turtle.Turtle()
hunter.shape("left.gif")
hunter.penup()
hunter.goto(0,-150)

coin=turtle.Turtle()
coin.speed(1000)
coin.shape("coin.gif")
coin.penup()
coin.goto(-280,280)




def right():
    hunter.shape("left.gif")

    hunter.forward(5)


def left():
    hunter.shape("right.gif")
    hunter.backward(5)    


turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")


turtle.listen()

def move():
    y=coin.ycor()
    coin.sety(y-3)

while True:
    sea.update()
    move()    

    if coin.ycor() < -300 :
        x=random.randint(-280,280)
        coin.goto(x,280)
    
    
    
turtle.done()