from turtle import*
from random import  randint
speed(0)
goto(-140, 140)
penup()
for paso in range(14):
    write(paso, align='Center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ana = Turtle()
ana.color('red')
ana.shape ('turtle')

ana.penup()
ana.goto(-160,100)
ana.pendown()
    
   
gema = Turtle()
gema.color('pink')
gema.shape('turtle')

gema.penup()
gema.goto(-160,70)
gema.pendown()

luis = Turtle()
luis.color('black')
luis.shape('turtle')
luis.penup()
luis.goto(-160,40)
luis.pendown()

desbye = Turtle()
desbye.color('blue')
desbye.shape('turtle')

desbye.penup()
desbye.goto(-160,20)
desbye.pendown()

nazzi = Turtle()
nazzi.color('orange')
nazzi.shape('turtle')

nazzi.penup()
nazzi.goto(-160,10)
nazzi.pendown()


for turn in range(100):
        ana.forward(randint(1,5))
        gema.forward(randint(1,5))
        luis.forward(randint(1,5))
        desbye.forward(randint(1,5))
        nazzi.forward(randint(1,5))

for giro in range(8):
  ana.left(randint(1,5))
  gema.right(randint(1,5))
  luis.right(randint(1,5))
  desbye.right(randint(1,5))
  nazzi.right(randint(1,5))