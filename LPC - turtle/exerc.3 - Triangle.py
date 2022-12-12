import turtle


# Screen Settings
sc = turtle.Screen() 
tess = turtle.Turtle() 
 
 
def triangle(x,y):
   
    # To Draw the Triangle
    tess.penup()
    tess.goto(x,y)
    tess.pendown()
    
    for i in range(3):

        # Moving the cursor 
        tess.forward(100)
        tess.left(120)
        tess.forward(100)
         
# Final Settings
turtle.onscreenclick(triangle,1)
 
turtle.listen()
 
turtle.done()