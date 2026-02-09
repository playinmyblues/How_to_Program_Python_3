# This file contains exercises from the PDF for chapter 5. This chapter works with while loops
# and for loops.
# 1
print("#1")
i = 10
while i > 1:
    print("i: ", i)
    i /= 2

# 2
print("#2")
i = 0
value = 0
while value < 20:
    value += i
    i += 1
    print("value: ", value)

# 3
print("#3")
for i in range(4):
    print("i: ", i)
# prints 0 to 3

# 4
print("#4")
for i in range(3, 5):
    print("i: ", i)
# prints 3 and 4

# 5
print("#5")
for i in range(1, 10, 3):
    print("i: ", i)
# prints 1, 4, 7

# 6
print("#6")
for i in range(1, 10, -3):
    print("i: ", i)
# prints 1 - ACTUALLY, prints nothing

# 7
print("#7")
for i in range(10, 1, -3):
    print("i: ", i)
# prints 10, 7, 4

# 8
# Get a number from the user, and then count from 1 to that number. Try writing
# it using both a while loop and a for loop.
print("#8")
limit = int(input("Please enter a number greater than 0: "))
print("while loop:")
i = 0
while i < limit:
    print("i: ", i)
    i += 1
print("for loop:")
for i in range(limit):
    print("i: ", i)

# 9
# Convert the following while loop into a for loop.
print("#9")
print("while loop example")
i = 2
while(i<7):
    print("i: ", i)
    i = i + 3

print("converted to for loop")
i = 2
for i in range(i, 7, 3):
    print("i: ", i)

# 10
# Write a short program that defines a number from 1 to 10, and then keeps
# asking the user to guess that number until the correct number is guessed.
# the following line is normally provided at the top of the code to import the library or just one
# function within that library
import random
print("#10")
number_to_guess = random.randint(1, 10)
# print("number_to_guess:", number_to_guess) - just here to verify the code works
user_guess = int(input("Please guess a number between 1 and 10, inclusive: "))
print("Your guess is: ", user_guess)
while user_guess != number_to_guess:
    if(user_guess < number_to_guess):
        print("Your guess was too low.")
    else:
        print("Your guess was too high.")
    user_guess = int(input("Please guess again: "))
print("Your user_guess of", user_guess, "was correct!")