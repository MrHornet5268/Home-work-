#A4C2.) So this is just multiplying the number by itself generates numbers 0 to 4, and for each number,
# the program multiplies the number by itself (i * i) and prints the Result 0,1,4,9,16.
for i in range(5):
    print(i * i)
print()

#B4C2.) This code puts all the numbers on the same line becausce of the end="" and prints 3 1 4 1 5 with spaces 
for d in [3, 1, 4, 1, 5]:
    print(d, end=" ")
print()
print()
#C4C2.) This show how the program counts how many times you what to say Hello and Result would be this
# Hello
# Hello
# Hello
# Hello
for i in range(4):
    print("Hello")
print()
print()
#D4C2.) This shows how the program calculates and gets risen by 2 for the result of the number. Result would be this
# 0 1
# 1 2
# 2 4
# 3 8
# 4 16
for i in range(5):
    print(i, 2 ** i)
print()
print()
#Chapter 3
#A1C3.)it will show you the proper form in Float because you would divdie frist then muplite  then add in the form of PEMDAS Which then would Adding these gives the final result of 7.4.
one = 4.0 / 10.0 + 3.5 * 2
print(one)
print()
#C1C3.) This is a legal one because the statement uses vaild integer in multiple math fileds  and will show in integer form.
two = abs(4 - 20 // 3) * 2
print(two)
print()
#E1C3.) this is legal because they show vaild operations to do the math and show the proper integer.
three = 3 * 10 // 3 + 10 % 3
print(three)
print()
n=3
r=1
import math
# for these problems didnt say if they needed to be print or not and had to put numbers for the letter or it would be a error its saids.
#B2C3.) since the n is outside the the () we know its mupiltes then after we times the ouside by the inside numbers then we get the answenr divdie by 2 to get the answer
(n * (n - 1)) / 2
print()
#C2C3.) 4 is the number we where off with then math.pi is the code for pie when import math comes in and the ** 2 gets you the r^2 
4 * math.pi * r ** 2
print()
#B4C3.) it will show a loop of each number and it will do the number : and the cuded answer. Result would be this
# 1 : 1
# 3 : 27
# 5 : 125
# 7 : 343
# 9 : 729
for i in [1, 3, 5, 7, 9]:
    print(i, ":", i**3)
print()
#C4C3.) It will generates a numbers from 0 to 9 and the end will print the range numbers and then the x+y will add and print the number and it will print done
x = 2
y = 10
for j in range(0, y, x):
    print(j, end="")
print(x + y)
print("done")
print()
#PE6C3
# put the first point you want (x1, y1)
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
# put the second point you want (x2, y2)
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate the X and Y's to see if we get perfect vertical line
iny = y2 - y1
inx = x2 - x1

# Check if the line is vertical
if inx == 0:
    print("The line is a perfect vertical line so the slope is Undefined.")
    print()
#PE7C3
else:
    # this calculates the slope if it gets pass the vertical line part
    slope = iny / inx
    print("The slope of the line is:", slope)
print()
import math
    # Input coordinates for two points of x1-y2
ix1 = float(input("Enter x1: "))
iy1 = float(input("Enter y1: "))
ix2 = float(input("Enter x2: "))
iy2 = float(input("Enter y2: "))
print()
# Calculate distance of the X's and Y's
dis = ((ix2 - ix1)**2 + (iy2 - iy1)**2)**0.5
# The answer to the Distance question
print("The distance between the points is:", round(dis, 2))
