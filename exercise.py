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



