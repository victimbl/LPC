from turtle import * 
  
speed('fastest')
  
# Turtle Setup
rt(-90)
angle = 30
  
# Plotting a Y
def tree(sz, level):   
  
    if level > 0:
        # Setting the colour
        colormode(255)
        pencolor(0, 255//level, 0)
          
        # Base
        fd(sz)
        rt(angle)
  
        # Right Side
        tree(0.8 * sz, level-1)          
        pencolor(0, 255//level, 0)
        lt( 2 * angle )
  
        # Left Side
        tree(0.8 * sz, level-1)
        pencolor(0, 255//level, 0)
        rt(angle)
        fd(-sz)
           
          
# Drawing the Tree
tree(80, 7)