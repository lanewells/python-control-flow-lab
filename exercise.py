# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    letter = input('Enter a letter of the alphabet: ').lower()
    vowel = list("aeiou")
    character = list('"`~!@#$%^&*()_+=-[]}{\|;:<.,>?/ ')
    if letter in vowel:
        print(f'The letter "{letter}" is a vowel.')
    elif letter == "y":
        print(f'The letter {letter} MIGHT be a vowel...')
    elif letter.isdigit() or len(letter) > 1 or letter in character:
        print(f'The character "{letter}" is not a single letter of the alphabet. Please try again.')
    else:
        print(f'The letter {letter} is a consonant.')

# Call the function
# check_letter()
#

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    age = input('Please enter your current age: ')
    eligible_age = 18
    if not age.isdigit() or int(age) < 0:
         print('Please enter a valid and positive whole number.')
    elif int(age) >= eligible_age:
        print(f'You are eligible to vote, as you are {age} years old.')
    else:
        print(f'You are {age} years old, which means you are ineligible to vote. We look forward to seeing you when you turn {eligible_age}!')

# Call the function
# check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    dog_age = input("Enter dog's age: ")
    if not dog_age.isdigit() or int(dog_age) < 0:
        print('Please enter a valid and positive number.')
        return
    dog_age = int(dog_age)
    if 2 >= int(dog_age):
        dog_age *= 10
    else: 
        dog_age = 20 + (dog_age -2) * 7
    print (f"Dog's age is {dog_age} in dog years!")

# Call the function
# calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here

    cold = input('Is it cold? (yes/no)')
    raining = input('Is it raining? (yes/no)')

    if cold == "yes" and raining == "yes":
        print('Wear a waterproof coat.')
    elif cold == "yes" and not raining == "yes":
        print('Wear a warm coat.')
    elif not cold == "yes" and raining == "yes":
        print('Carry and umbrella.')
    elif not cold == "yes" and not raining == "yes":
        print('Wear light clothing.')


# Call the function
# weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    mmm = input('Enter the month of the year following this format (Jan - Dec): ').capitalize()
    dd = int(input ('Enter the date of the month in digits: '))
    
    if mmm not in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
        print('Please enter a valid month')
        return
    if not 1 <= dd <=31:
        print('Please enter a valid date between 1 and 31.')
        return
        
    if (mmm == 'Dec' and dd >= 21) or (mmm == 'Mar' and dd <= 19) or mmm in ('Jan', 'Feb'):
        season = 'Winter'
    elif (mmm == 'Mar' and dd >= 20) or (mmm == 'Jun' and dd <= 20) or mmm in ('Apr', 'May'):
        season = 'Spring'
    elif (mmm == 'Jun' and dd >= 21) or (mmm == 'Sep' and dd <= 21) or mmm in ('Jul', 'Aug'):
        season = 'Summer'
    elif (mmm == 'Sep' and dd >= 22) or (mmm == 'Dec' and dd <= 20) or mmm in ('Oct', 'Nov'):
        season = 'Fall'
    else:
        print('The date you entered is not valid.')
        return
    
    print(f'{mmm} {dd} is in {season}.')
        
# Call the function
determine_season()
