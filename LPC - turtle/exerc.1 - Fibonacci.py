import turtle
import math
 

def fibonacci(n):
    a = 0
    b = 1
    square_a = a
    square_b = b
    
    # Pen colour for Squares
    x.pencolor("blue")
 
    # First Square
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
 
    # Fibonacci Series
    temp = square_b
    square_b = square_b + square_a
    square_a = temp
     
    # Rest of the Squares
    for i in range(1, n):
        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
 
        # Fibonacci Series
        temp = square_b
        square_b = square_b + square_a
        square_a = temp
 
    # Pen at start point
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()
 
    # Pen colour for the Spiral
    x.pencolor("red")
 
    # Fibonacci Spiral
    x.left(90)
    for i in range(n):
        print(b)
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        temp = a
        a = b
        b = temp + b
  
 
# The Factor that will change the Scale
factor = 1
 
# Number of Interactions
n = int(input('Enter the number of iterations (must be > 1): '))
 
# Producing the Fibonacci Spiral and its Number
if n > 0:
    print("Fibonacci series for", n, "elements :")
    x = turtle.Turtle()
    x.speed(100)
    fibonacci(n)
    turtle.done()
else:
    print("Number of iterations must be > 0")