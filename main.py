# ============================================================
# Python Final Project 2026
# Name: Yoshimi Chick
# Date: 5/7/2026
# Project Title: 
# Description: (Write 1-2 sentences explaining what your program does)
# ============================================================


# ---- SECTION 1: Setup / Variables ----
# Create your starting variables here.
# Example: player_name = ""
name = input("What is your name?:")
# The code is asking for the user's name.


# ---- SECTION 2: Welcome Message ----
# Greet the user and explain what your program does.

print("Welcome", name)
print("This program is designed to take your assignment scores and calculate then into a grade.")
schoolClass = input("What class is this grade for?:")
# The code  is letting the user know what it does and it greets them.

# ---- SECTION 3: Get Input from User ----
# Use input() to ask the user for information.
# Remember: input() always returns a string.
# Use int() or float() if you need a number.

# Example:
# player_name = input("What is your name? ")
# score = int(input("Enter a number: "))
gradeOne = float(input("What is your first grade in percenage? Do not include the % mark:"))
gradeTwo = float(input("What is your second grade in percentage? Do not include the % mark:"))
gradeThree =float(input("What is your third grade in percentage? Do not include the % mark:"))

finalGrade = (gradeOne + gradeTwo + gradeThree) /3

print("Your overall grade average for", schoolClass, "is", finalGrade)

# In this section the code is gathering your three grades and averaging them out.

# ---- SECTION 4: Logic (if / elif / else) ----
# Use if/elif/else to make decisions based on user input or variables.

# Example:
# if score >= 90:
#     print("Great job!")
# elif score >= 70:
#     print("Good work!")
# else:
#     print("Keep practicing!")
if finalGrade == 67:
    print("You did that on purpose, didn't you? I'm dissapointed.")
if finalGrade >= 90:
    print("You have an A")
elif finalGrade >= 80:
    print("You have a B")
elif finalGrade >= 70:
    print("You have a C")
elif  finalGrade >= 60:
     print("You have a D")
else:
    print("You have a F")

# In this section the code is informing the user of their letter grade average.

# ---- SECTION 5: Final Output ----
# Print a final message, result, or summary to the user.

print("----------------------------")
print("Thanks for using my program! Good luck in your class")

#The code is ending.