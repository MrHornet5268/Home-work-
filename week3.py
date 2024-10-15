#PE13C3
def allnumbers():
#talks about how much numbers you want to add
    count = int(input("How many numbers do you want to add? "))

#start the sum at 0
    total= 0

#ask the user for how many each number to add the total sum
    for i in range(count):
         number = float(input("Enter a number: "))
         total += number  
         print()
#print the final sum
    print("The total sum is:", total)
    print()

allnumbers()

#PE14C3
def avnumbers():
    #ask the user how many numbers they want to put to find the average of
    count = int(input("How many numbers do you want to average? "))

    #start the sum at 0
    total = 0

    #loop to ask for each number and add it to the total sum
    for i in range(count):
        number = float(input("Enter a number: "))
        total += number  

    #find the average by dividing the total by the number of numbers
    average = total / count

    #print the final average
    print("The average is:", average)
    print()
# Run the program
avnumbers()

#DP2C4
#a) Point(130, 130): Shows a small dot being form on the x and y coordinates showen
#b) c = Circle(Point(30, 40), 25) c.setFill("blue") c.setOutline("red"): it will show a red outline cricle with blue on the inside of the shape.
#c) r = Rectangle(Point(20, 20), Point(40, 40)) r.setFill(color_rgb(0, 255, 150)) r.setWidth(3): will Show a square and it will show to the left corner to the right corner will be filled with a greenish color.
#d) l = Line(Point(100, 100), Point(100, 200)) l.setOutline("red4") l.setArrow("first"): Is a straight line with a red color and has a arrow at the starting point.
#e) Oval(Point(50, 50), Point(60, 100)): it will just show a Oval with no color because none is said.
#f)shape = Polygon(Point(5, 5), Point(10, 10), Point(5, 10), Point(10, 5)) shape.setFill("orange"): will show a Polygon filled with a orange color with the points said connecing to one another
#g) t = Text(Point(100, 100), "Hello World!") t.setFace("courier") t.setSize(16)t.setStyle("italic"): will show a text message box with the saying hello world with a different style of font.

#DP3C4
# The red circle follows will the user clicks and when the user clicks 10 times the window shuts down.


#PE2C4
from graphics import *

def Targets():
    win = GraphWin("Archery Target", 400, 400)
    center = Point(200, 200)  # Center 
    radius = 40  

    # Draw rings
    colors = ["white", "black", "blue", "red", "yellow"]
    for i in range(5, 0, -1):
        Circle(center, radius * i).draw(win).setFill(colors[5 - i])

    win.getMouse()  
    win.close()

Targets()

#PE3C4
from graphics import *

def face():
    win = GraphWin("Face", 400, 400)

    # Head 
    Circle(Point(200, 200), 100).draw(win).setFill("tan")

    # Mouth 
    Oval(Point(160, 250), Point(240, 280)).draw(win).setFill("pink")

    # Nose 
    Polygon(Point(200, 190), Point(190, 210), Point(210, 210)).draw(win).setFill("white")

   # Left Eye 
    Circle(Point(160, 170), 15).draw(win).setFill("brown")

    # Right Eye 
    Circle(Point(240, 170), 15).draw(win).setFill("brown")
    win.getMouse()  
    win.close()

face()

#PE8C4
from graphics import *
import math

def line():
    win = GraphWin("Line Info", 400, 400)

    # Get two points
    p1 = win.getMouse()
    p2 = win.getMouse()

    # Draw the line and points
    Line(p1, p2).draw(win)
    Point(p1.getX(), p1.getY()).draw(win).setFill("black")
    Point(p2.getX(), p2.getY()).draw(win).setFill("black")

    # Midpoint
    mx = (p1.getX() + p2.getX()) / 2
    my = (p1.getY() + p2.getY()) / 2
    Point(mx, my).draw(win).setFill("cyan")

    # Length and slope
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    length = math.sqrt(dx**2 + dy**2)
    slope = dy / dx if dx != 0 else "inf"
    Text(Point(200, 350), f"Length: {length:.2f}, Slope: {slope}").draw(win)

    win.getMouse()  
    win.close()

line()


