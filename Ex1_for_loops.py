# -------------------------------------------
# Exercise 1: For Loops
# -------------------------------------------
# In this exercise, you’ll learn how to repeat actions using a for loop.
# A for loop is used when you know *how many times* you want to repeat something.
#
# Syntax reminder:
# for variable in range(number):
#     # code that repeats
#
# Example (syntax only):
# for i in range(5):
#     print("This will print 5 times")
#
# You can also use variables and input inside loops to make your programs dynamic.
# -------------------------------------------

# Task 1: Simple Repetition
# -------------------------------------------
# In this task, you’ll make Python repeat a simple message.
# Example idea: printing your name or a short message several times.
#
# TODO:
# 1. Use a for loop with range() to print a message 5 times.
# 2. Inside the loop, print which repetition it is (e.g. "Message number 1").
# 3. Use the loop variable (often called i) in your message.
#
# Example (similar idea, not the answer):
# for i in range(3):
#     print("Hello number", i)
#
# Write your code below:
print()
print("Exercise 1")
print()
print("Task 1")
print()
print("Loops for pre-determined number of times")
print()
for i in range(5):
    print("Message number ", i)
print()

# Task 2: Counting with for loops
# -------------------------------------------
# You can use range() to count numbers up or down.
#
# TODO:
# 1. Use a for loop with range() to print numbers from 1 to 10.
# 2. Then, write another loop that counts down from 10 to 1.
# 3. Print a message before and after the loop (for example: "Counting up..." and "Counting down...").
#
# Example (similar idea):
# for i in range(1, 6):
#     print(i)
#
# Write your code below:
print("Task 2")
print()
print("Counting from 1 to 10")
print()
for i in range(1, 11):
    print(i)
print()
#
print("Counting down from 10 to 1")
for i in range(10, 0, -1):
    print(i)
print()
# Task 3: Using for loops with user input
# -------------------------------------------
# You can combine input() with for loops.
#
# TODO:
# 1. Ask the user how many times they want to repeat a message.
# 2. Use that number in range() to repeat a message that many times.
# 3. Include the loop counter in the message (so the user can see which loop number it is).
#
# Example (similar idea):
# for i in range(user_number):
#     print("This is loop", i + 1)
#
# Write your code below:
print("Task 3")
print()
print("Repeating a message using a User input")
print()
number = int(input("Please enter a number "))
for i in range(number):
    print("This is loop", i + 1)
print()

# -------------------------------------------
# Submitting Your Work (after Tasks 1–3)
# -------------------------------------------
# Once you’ve completed the 3 basic tasks:
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex1_for_loops.py
#    git commit -m "Completed for loop basic tasks"
#    git push origin main
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1:
# -------------------------------------------
# Ask the user for a word.
# Use a for loop to print each letter of that word on a separate line.
# Example idea:
# Input: "cat"
# Output:
# c
# a
# t
#
# Hint: You can loop directly over a string like this:
# for letter in word:
#     print(letter)

# Write your code below:
print("Extension 1")
print()
print("Printing a user defined word into seperate lines")
print()
word = input("Please enter a word ")
for letter in word:
    print(letter)
print()

# Extension 2:
# -------------------------------------------
# Ask the user to enter a number.
# Use a for loop to print all even numbers from 0 up to that number (inclusive).
# Hint: You can use range(start, stop, step) — for example, range(0, 10, 2)

# Write your code below:
print("Extension 2")
print()
print("Printing all the even numbers from 0 to a user defined number")
print()
number = int(input("Choose a number "))
for i in range(0, number, 2):
    print(i)
(print)

# Extension 3 (a bit harder):
# -------------------------------------------
# Ask the user for their name.
# Use a for loop to print their name one letter at a time,
# BUT skip any spaces in their name using an if statement.
# Example:
# Input: "Mary Ann"
# Output:
# M
# a
# r
# y
# A
# n
# n

# Write your code below:
print("Extension 3")
print()
print("Printing a user defined name while skipping any blank spaces")
print()
name = input("Please enter your Christian and Surname ")
for letter in name:
    if letter != ("", -1):
        print (letter)
#print("Unfortunately this doesn't work! I couldn't figure it out!)
print()

# -------------------------------------------
# ADVANCED ACTIVITY
# -------------------------------------------
# Create a mini “times table” program.
# 1. Ask the user for a number (e.g. 7)
# 2. Use a for loop to print that number multiplied by 1 to 10.
# Example (if user enters 3):
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# ...
# 3 x 10 = 30
#
# Hint: use f-strings to format the output neatly, e.g.
# print(f"{num} x {i} = {num * i}")

# Write your code below:
print()
print("Advanced activity")
print()
start=1
end=11
count=0
number = int(input("Please enter a number "))
for i in range(start, end, count +1):
    print(f"{number * i}")
print()


# -------------------------------------------
# Submitting Your Work (after Extensions & Advanced)
# -------------------------------------------
# Once you’ve completed all tasks:
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex1_for_loops.py
#    git commit -m "Completed for loop extensions and advanced activity"
#    git push origin main
# Check GitHub to confirm your changes appear.
# -------------------------------------------
