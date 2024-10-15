
s1 = " spam"
s2 = "ni !"

#DP1C5
#C) s1[1]: This shows you the second chacrter of s1 which would result in s
C = s1[1]
print (C)
print()
#E) 1 [2] + s2 [:2]: This shows the combine characters of the index e of s1 with characters of s2 which resulting in pni
E = s1[2] + s2[:2]
print (E)
print()
#G)s1.upper(): This changes all the letters in s1 to big letters, so you get " SPAM"
G = s1.upper()
print (G)
print()
#DP2C5
#A) Gets 'n' and 'i', turns them into a capitalize letters 'NI', and adds a space.
A = s2[:2].upper() + ' '  
print (A)
print()
#D)just really print spam after using the s1
D = s1
print(D)
print()
#E)Takes the first three characters sp and the fourth character a, making a list: [' sp ', 'a']
e = [s1[:3], s1[3]]
print (e)
print()
#DP3C5
#B: the split prints each word in the string on a new line
for w in "Now is the winter of our discontent . . . " . split ( ) :
    print (w)
print()
#C split the word by the i so it dosen't show the i's and split them up
for w in "Mississippi".split("i"):
    print(w, end=" ")
    print()
#E should put the would secert into a code and moving down the lettter by one
msg = ""
for ch in "secret":
    msg = msg + chr(ord(ch) + 1)
print(msg)
print()
#own problem: This program uses five loops to print 60 "F"s, 10 "D"s, 10 "C"s, 9 "B"s, and 10 "A"s all on the same line
print('grades = "', end='')

for i in range(60):
    print('F', end='')

for i in range(10):
    print('D', end='')

for i in range(10):
    print('C', end='')

for i in range(9):
    print('B', end='')


for i in range(10):
    print('A', end='')

print()
#PE3C5
grades = "FFFFFFDCBA"

# Get the user score from the user input
score = int(input("Enter the exam score (0-100): "))

# This ensure that the score is within the valid range of the grades
if score > 100:
    score = 100

# Dividing score by 10 to get an a accurate grade 
grade = grades[score // 10]

print("The user grade is: ",grade)
print()
#PE4C5
# the user will type a sentence
phrase = input("Type a sentence: ")

# Split the sentence the user said into words
words = phrase.split()

# will get an empty acronym
acronym = ""


for word in words:
    # Take the first letter, make it uppercase, and add it to the acronym
    acronym += word[0].upper()

# the final outcome
print("Your acronym is:", acronym)
print()
#PE5C5
# Ask the user to type a name
name = input("Type a name: ")

# Start with 0 value
total_value = 0

# Look at each letter in the name
for letter in name.lower():  #  will make it all lowercase 
    if letter.isalpha():  #will react to real letters, ignore spaces or symbols
        total_value += ord(letter) - ord('a') + 1  

# Show the total value of the name
print("The value of the name is:", total_value)



