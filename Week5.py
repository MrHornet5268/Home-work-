#Q1PE1C6
# This is the function to print the song lyrics
def old_macdonald(animal, sound):
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    print("And on that farm he had a " ,animal, ", Ee-igh, Ee-igh, Oh!")
    print("With a " ,sound, ", " ,sound, " here and a " ,sound, ", " ,sound, " there.")
    print("Here a " ,sound, ", there a " ,sound, ", everywhere a " ,sound, ", " ,sound, ".")
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    print()  

# Each function for each animal
old_macdonald("cow", "moo")
old_macdonald("pig", "oink")
old_macdonald("duck", "quack")
old_macdonald("sheep", "baa")
old_macdonald("horse", "neigh")

print()
#Q2EP14C3
# Function to get numbers from user calculate the sum and return the average
def com_average(count):
    total_sum = 0  # Start with 0 sum
    for i in range(count):
        num = float(input("Enter a number: "))  # Ask user for a number
        total_sum += num  
    return total_sum / count  

# The program
how_many = int(input("How many numbers do you want to enter? "))  # Ask how many numbers
average = com_average(how_many)  
print("The average of the numbers is:", average)  #average
print()

#Q3EP8C4
import math

# Function to calculate slope
def c_slope(dx, dy):
    return dy / dx if dx != 0 else float("inf")

# Function to calculate distance for the Length
def c_distance(dx, dy):
    return math.sqrt(dx**2 + dy**2)

# This function is to get the user input and calculate slope and distance
def main():
    print("Also you need to put a space after you type on the frist point or the program will not work.")
    x1, y1 = map(float, input("Enter the first points (x1, y1): ").split())
    x2, y2 = map(float, input("Enter the second points (x2, y2): ").split())

    #differences
    dx = x2 - x1
    dy = y2 - y1

    # Calculate slope and distance
    slope = c_slope(dx, dy)
    distance = c_distance(dx, dy)

    # results
    print(f"Slope: {slope}")
    print(f"Length: {distance}")

main()

#Q4EP12C6
print()
def sumList(nums):
    total = 0
    for num in nums:
        total += num
    return total

# The code
nums = [2, 4, 6, 8, 10]
result = sumList(nums)
print(f"The sum of " ,nums ," is: " ,result,)
print()

#question 5
def get_some_strings(n):
    strings = []
    for i in range(n):
        s = input("Enter a string: ")
        strings.append(s)
    return strings

# Main part of the program
print("Please enter words of things you want to say for each string but only one")
num = int(input("How many strings will you enter? "))
result = get_some_strings(num)
print(result)

