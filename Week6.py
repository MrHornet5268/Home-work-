#C7DP2
#The similarities: try/except and if statements control the running flow of the program based on conditions, and peocssing them to determine which code to run.
#The Differences: The if statements check conditions for simple code, while try/except automatically handles unexpected errors, allowing for cleaner error management in code.


#C7PE3
# Exam score 
score = float(input("Enter the exam score (0-100): "))

# Determine the corresponding grade bast on this structures
if score >= 90 and score <= 100:
    grade = 'A'
elif score >= 80 and score < 90:
    grade = 'B'
elif score >= 70 and score < 80:
    grade = 'C'
elif score >= 60 and score < 70:
    grade = 'D'
elif score < 60 and score >= 0:
    grade = 'F'
else:
    grade = 'Invalid score'

# Print the corresponding grade
print("The corresponding grade is:" ,grade,)
print()
#C7PE7
 # Program to convert time 
def convert_to_minutes(hour, minute, period):
    if period.upper() == 'PM' and hour != 12:
        hour += 12  # Convert PM to 24-hour format
    elif period.upper() == 'AM' and hour == 12:
        hour = 0  # Convert 12 AM to 0 hours
    return hour * 60 + minute

# Calculating babysitting bill
def bill(start_hour, start_minute, start_period, end_hour, end_minute, end_period):
    start_time = convert_to_minutes(start_hour, start_minute, start_period)
    end_time = convert_to_minutes(end_hour, end_minute, end_period)

    # Rates
    rate_before_9 = 2.50  # rate until 9 PM
    rate_after_9 = 1.75   # rate after 9 PM
    cutoff_time = 21 * 60  # 9 PM in minutes

    total_bill = 0.0

    # Calculate total time in minutes
    for time in range(start_time, end_time):
        if time < cutoff_time:  # Before 9 PM
            total_bill += rate_before_9 / 60  # Prorate by the hour
        else:  # After 9 PM
            total_bill += rate_after_9 / 60  # Prorate by the hour

    return total_bill

# Input: Starting time and ending time
start_hour = int(input("Enter the starting hour (1-12): "))
start_minute = int(input("Enter the starting minute (0-59): "))
start_period = input("Enter AM or PM for starting time: ")

end_hour = int(input("Enter the ending hour (1-12): "))
end_minute = int(input("Enter the ending minute (0-59): "))
end_period = input("Enter AM or PM for ending time: ")

# Calculate total babysitting bill
total_bill = bill(start_hour, start_minute, start_period, end_hour, end_minute, end_period)

# Output the total bill
print("The total babysitting bill is: $",total_bill ,)
print()

#C7PE8
# Function to check eligibility for Senate and House
def eligibility(age, years_of_citizenship):
    # Check eligibility for Senate
    if age >= 30 and years_of_citizenship >= 9:
        senate_eligibility = "Eligible for the Senate"
    else:
        senate_eligibility = "Not eligible for the Senate"
    
    # Check eligibility for House of Representatives
    if age >= 25 and years_of_citizenship >= 7:
        house_eligibility = "Eligible for the House of Representatives"
    else:
        house_eligibility = "Not eligible for the House of Representatives"
    
    return senate_eligibility, house_eligibility

# Input: Get person's age and years of citizenship
age = int(input("Enter the person's age: "))
years_of_citizenship = int(input("Enter the number of years as a US citizen: "))

# Check eligibility
senate_eligibility, house_eligibility = eligibility(age, years_of_citizenship)

# Output the eligibility results
print(senate_eligibility)
print(house_eligibility)
print()
#Ch2Ex5 Part2
# Initial values

# Principal amount, compounding , and interest rate
P = 10000
n = 12     
r = 0.08

while True:
    try:
        # Get the number of years from the user for the compounded interest
        t = float(input("Enter the number of years: "))  # Ask for the number of years
        if t < 0:
            raise ValueError("Number of years cannot be negative. Please enter a positive value.")
        break  # Exit the loop if valid input is entered
    except ValueError:
        print("Invalid input. Please enter a valid number of years.")  # Error message for invalid input

# Shows the final amount using instrest
final_amount = P * (1 + r / n) ** (n * t)

# Print the final amount with two decimal places
print("\nThis is the final amount of money you will be compounded for after the years you entered: $", format(final_amount, ".2f"))

#Error one Invaild Input: If the user types something that isn’t a number the program doesn’t know what to do because it only understands numbers.
#How the Program Responds:  It catches the mistake and tells the user to try again with a proper number.

#Error two Negtive numbers: If the user enters a negative number like -5 for the number of years, it doesn't make sense because time can't be negative.
#How the Program Responds: It will stop and tells the user that the number of years can't be negative, asking them to enter a positive number instead.
