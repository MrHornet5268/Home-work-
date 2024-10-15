# A and B :One Has the , when it is printed while the other doesn't show it and add a space instead of ,
print("Hello, world!")
print("Hello", "world!")
print()
# C and D: C prints as an integer, while D prints as a decimal
print(3)
print(3.0)
print()
# E and F: E just add the numbers regular to form a normal 5 ,while F make a Float which is what happen when you have decimal values in coding
print(2 + 3)
print(2.0 + 3.0)
print()
# I and J: I dose multiplication to get 6, while J dose 2 times 2 times 2 to get you 8
print(2 * 3)
print(2 ** 3)
print()
# K and 2 // 3: K dose regular Division, while 2 // 3 it will give you the integer which would be less or equal to the answer given
print(7 / 3)
print(2 // 3)
print()
print()

#Ch1 Ex5

#what the program dose This program will show you what a chaotic function will look like,Please follow the dcrticions when the sentecne pop up
#Enter number here but stay in the rules or else it won't work. I have tried 
x = float(input("Enter a number between 0 and 1 (EX 0.5): "))

#The User enter will give you number values
n = int(input("How many numbers should I print today? "))

# Loop to redo the number conmaned 
for i in range(n):
    x = 3.9 * x * (1 - x)  
    print(x)
    
#Ch2 Ex10
print()
kilometers = float(input("Enter the distance in kilometers: "))
print()
# Convert kilometers to miles
Miles = kilometers * 0.62
print ("This is what you get when you put the number you want to convert from kilometers into miles!:",Miles," Miles")
print()
print()
#Ch2 Ex5 HTTLACS
# Principal amount, compounding frequency, and interest rate
P = 10000
n = 12
r = 0.08

# Get the number of years from the user for the compounded instertest 
t = float(input("Enter the number of years: "))
print()
# Print the final amount directly
number = (P * (1 + r / n) ** (n * t))
print ("This is the final amount of money you will be compounded for after the years you put above","$",number)
 
