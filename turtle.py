

import turtle 

bill = turtle.Turtle()
bill.speed(30)
distance = 5
width = 5
height = 10
bill.pencolor('darkblue')

bill.penup()

for y in range(height):
    for i in range(width):
        bill.pendown()
        # bill.forward(dot_distance)
    # bill.backward(dot_distance * width)
    bill.right(90)
    bill.forward(distance)
    bill.left(90)
bill.penup() 
for i in range(5):
  bill.forward(5)
for i in range(10):
    bill.pendown()
        # bill.forward(dot_distance)
    # bill.backward(dot_distance * width)
    bill.left(90)
    bill.forward(distance)
    bill.right(90)
bill.penup()
for i in range(10):

    bill.right(90)
    bill.forward(distance)
    bill.left(90)
bill.pendown()
for i in range(10):
  bill.forward(4)

bill.penup()

bill.forward(20)
bill.pendown()

for i in range(10):
    bill.pendown()
        # bill.forward(dot_distance)
    # bill.backward(dot_distance * width)
    bill.left(90)
    bill.forward(distance-2)
    bill.right(90)
for i in range(10):
    bill.left(60)
    bill.forward(distance-2)
    bill.right(60)
for i in range(10):
    bill.left(60)
    bill.backward(distance-2)
    bill.right(60)
for i in range(10):
    bill.right(60)
    bill.backward(distance-2)
    bill.left(60)
    
    
turtle.done()