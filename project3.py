'''
Ella Anderson
For this project I used the functions to draw a Horse under the Sea
After Refactoring I decided to add more fish and another horse
I did this without AI so the replica of the original scene I created isnt exact but it got kind of complicated with
the placement so I did my best
'''


# loads the Turtle graphics module, which is a built-in library in Python
import turtle
import math

def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen


def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_square(t, size, fill_color=None):
    """Draw a square with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    """Draw an equilateral triangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    """Draw a circle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()


def draw_polygon(t, sides, size, fill_color=None):
    """Draw a regular polygon with given number of sides"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()

def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    """
    Draw a curved line using small line segments
    
    Parameters:
    - t: turtle object
    - length: total length of the curve
    - curve_factor: positive for upward curve, negative for downward curve
    - segments: number of segments (higher = smoother curve)
    - fill_color: optional color to fill if creating a closed shape
    """
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
        
    segment_length = length / segments
    # Save the original heading
    original_heading = t.heading()
    
    for i in range(segments):
        # Calculate the angle for this segment
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)  # Reset the angle for the next segment
    
    # Reset to original heading
    t.setheading(original_heading)
    
    if fill_color:
        t.end_fill()
        
def jump_to(t, x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()

# My Functions

def Horse(t, x, y, size, c_body="brown", c_hair="black"):
    # Variables
    '''
    I want the x and y parameter to choose where the horse's left foot will be
    But the rectangle function starts at the top right corner so i tried my best
    '''
    height = size/2
    y = y+height+(size/2)
    y_leg = y - height
    x_neck = x+size-size/4

    # Body
    jump_to(t,x,y)
    draw_rectangle(t,size,height,c_body)
    jump_to(t,x,y_leg)
    draw_rectangle(t,size/4,height,c_body)
    jump_to(t,x_neck,y_leg+size)
    draw_rectangle(t,size/4,size*1.5,c_body)
    jump_to(t,x_neck+size/4,y_leg+size-size/5)
    draw_circle(t,size/4,c_body)
    
    # Eye
    t.pu()
    t.setheading(90)
    t.fd(size/5)
    t.pd()
    draw_circle(t,5,"black")

    # Hair
    t.setheading(0)
    jump_to(t,x_neck-size/10,y_leg+size*1.1)
    draw_rectangle(t,size/10,size/2,c_hair)
    jump_to(t,x-size/10,y)
    draw_square(t,size/10,c_hair)
    jump_to(t,x-size/5,y)
    draw_rectangle(t,size/10,size/2,c_hair)

    # Reset Pen
    t.setheading(0)
    t.pu()

def Fish (t, x, y, sides, size, c_body="yellow", c_tail="black"):

    # Draw the body
    jump_to(t,x,y)
    draw_polygon(t,sides,size,c_body)

    # Drawing the Tail
    ''' 
    I don't know how to calculate the area in a general function for every shape that is possible so instead I
    recreated the polygon function and tried to put the tail at the halfway point
    '''
    jump_to(t,x,y)
    t.pu()
    angle = 360 / sides
    for i in range(sides):
        t.forward(size)
        t.right(angle)
        if i == (sides/2)+1 or i == ((sides+1)/2):
            t.fd(size/2)
            t.setheading(180)
            t.pd()
            draw_triangle(t,size,c_tail)
        t.pu()

    # Drawing the Eye
    jump_to(t,x,y)
    t.pu()
    t.setheading(0)
    for i in range(2):
        t.fd(size)
        t.right(angle)
    t.setheading(180)
    t.fd(size/3)
    if sides >= 7:
        t.setheading(270)
        t.fd(size/3)
        draw_circle(t,5,"black")
    else:
        t.setheading(90)
        t.fd(size/3)
        draw_circle(t,5,"black")

    # Reset the Pen
    t.setheading(0)
    t.pu()



def Fish2 (t, x, y, length, width, c_body="light blue", c_tail="red", right=True):
    
    # Draw the Body
    jump_to(t,x,y)
    draw_rectangle(t,length,width,c_body)
    
    # Position the Tail based on choice
    t.pu()
    t.setheading(270)
    t.fd(width/2)
    if right == False:
        t.setheading(0)
        t.fd(length)
    else:
        t.setheading(180)
        t.fd(width)
        t.setheading(0)
    draw_triangle(t,width,c_tail)
    
    # Position the Eye Based on choice
    jump_to(t,x,y)
    t.pu()
    if right == True:
        t.fd(length-(length/3))
    else:
        t.fd(length/3)
    t.setheading(270)
    t.fd(width/3)
    t.pd()
    draw_circle(t,5,"black")
    
    # Reset the Pen
    t.setheading(0)
    t.pu()


def Bubbles (t, x, y):
    c = "white"
    o = x
    for i in range(5):
        jump_to(t,x,y)
        draw_circle(t,5,c)
        if i == 1 or i == 3:
            x = o
        else:
            x += 25
        y += 25

def Seaweed (t, x, y=-125, amm=5):
      jump_to(t, x, y)
      c = "lime green"
      for i in range(amm):
        jump_to(t,x,y)
        draw_rectangle(t,10,25,c)
        jump_to(t,x+10,y-25)
        draw_rectangle(t,10,25,c)
        jump_to(t,x,y-50)
        draw_rectangle(t,10,25,c)
        x += 50

def Ground (t,x=-500,y=-200,c="#e6d57f"):
    jump_to(t,x,y)
    draw_rectangle(t,1000,200,c)


#YOU MUST add function calls in this draw_scence function defintion
# to create your scence (No statements outside of function definiions)
def draw_scene(t):
    """Draw a colorful scene with various shapes"""
    # Set background color
    screen = t.getscreen()
    screen.bgcolor("skyblue")

    # My Functions
    
    # Original Scene
    '''
    Fish(t,-200,200,8,25)
    Bubbles(t,-120,175)
    Fish2(t,100,10,50,20,right=False)
    Bubbles(t,75,0)
    Seaweed(t,0,-125)
    Horse(t,-200,-200,100)
    Ground(t)
    '''

    # Upgraded Scene
    Fish(t,-200,200,9,30,"pink")
    Bubbles(t,-120,150)
    Fish(t,200,100,6,20)
    Bubbles(t,250,50)
    Fish2(t,100,20,50,25,right=False)
    Bubbles(t,50,0)
    Fish2(t,-10,-10,30,10,"red","blue")
    Horse(t,-200,-200,50,"pink","yellow")
    Horse(t,-300,-200,100)
    Seaweed(t,50,-125)
    Ground(t)


# This is the main() function that starts off the execution
def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()

# if this script is executed, call the main() function
# meaning when is file is run directly
if __name__ == "__main__":
    main()