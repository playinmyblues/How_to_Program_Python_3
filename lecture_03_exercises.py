# This Python file is used to do the exercises from this course's PDF for Chapter 3.

#1:
a = 1
b = 2
c = 2
d = "One"
e = "Two"
f = "Three"
g = "one"

# printing out the values of the boolean experessions
result1 = a > b
print(result1)
result2 = a == b # False
print(result2)
result3 = a != b    # True
print(result3)
result4 = b == c    # True
print(result4)
result5 = d < e     # True - but why? If I put another O at the start of "One" -> "OOne"
# the result is True. If I put a U at the start of "One" -> "UOne", the answer is False.
# I suspect that it evaluates strings alphabetically, with letters near the beginning of the
# alphabet having higher value than those closer to the end of the alphabet.
print(result5)
result6 = e < f     # True
print(result6)
result7 = d < g     # True - I think lowerercase letters rank higher than uppercase letters
print(result7)
result8 = g < e     # True
print(result8)
result9 = not(a == b)   # True
print(result9)
result10 = b < c or b > c   # False - b is equivalent to c
print(result10)
result11 = (a+1) == b and not b < c     # True
print(result11)
result12 = ((a <= b) and (b <= c)) or ((a >= b) and (b >= c))   # True
print(result12)

# 13
total_cost = 100.00
days = 3
cost_per_day = total_cost / days
if cost_per_day > 40:
    print("Too expensive")
elif cost_per_day > 30:
    print("Reasonable cost")
elif cost_per_day > 20:
    print("Excellent cost")
else:
    print("Incredible bargain")

# 14
age = 67
income = 10000
if (age > 70):
    if (income < 15000):
        print("Eligible for benefits")
    else:
        if (income < 20000):
            print("Eligible for reduced benefits")
        else:
            print("Not eligible for benefits")
else:
    if (income < 20000):
        print("Eligible for reduced benefits")
    else:
        print("Not eligible for beenfits")

# 15 - Rewrite the code in exercise 14 in a simpler way by using a more complex
# Boolean expression and an elif statement.
age = 67
income = 10000
if (income < 15000) and (age > 70):
    print("Eligible for benefits")
elif (income < 20000) and (age > 70):
    print("Eligible for reduced benefits")
elif (income < 20000):
    print("Eligible for reduced benefits")
else:
    print("Not eligible for benefits")

# 16 - Compare a variable “user_guess” to a variable “hidden_answer,” and tell the
# user whether the guess is too low, too high, or exactly right.
hidden_answer = 7423
user_guess = input("Please enter your best guess for an integer anywhere in the range of 0 to 10000: ")
user_guess = int(user_guess)
if (user_guess > hidden_answer):
    print("Your guess was too high")
elif (user_guess < hidden_answer):
    print("Your guess was too low")
elif (user_guess == hidden_answer):
    print("Your guess was exactly the answer.")

# 17 - Generally, every fourth year is a leap year, but there are exceptions. If the
# year is divisible by 100, then it is not a leap year, unless the year is also
# divisible by 400, in which case it is still a leap year. So, 2000 (divisible by
# 400) is a leap year, 2100 (divisible by 100 but not 400) is not, 2004 (divisible
# by 4 but not 100) is a leap year, and 2001 (not divisible by 4) is not. Write code
# that examines a variable and year and prints out “Leap year” or “Not a leap
# year” for that value. Try writing the code in the following three different ways.
# a) As a series of nested if statements
# b) As a set of if-elif-else statements
# c) As a single if statement with a complex Boolean expression
print()
print("This program will determine if your year is a leap year.")
the_year = int(input("What year is your year? "))

# part a)
print("part a)")
if (the_year % 4) == 0:
    if (the_year % 10) == 4 or (the_year % 10) == 8 or (the_year % 10) == 0:
        print(the_year, "is a leap year.")
    if (the_year % 100) == 0 and (the_year % 400) == 0:
        print(the_year, "is a leap year.")
    if (the_year % 100) == 0 and (the_year % 400) != 0:
        print(the_year, "is not a leap year")
else:
    print(the_year, "is not a leap year.")

# part b)
print("part b)")
if (the_year % 4) > 0:
    print(the_year, "is not a leap year.")
elif (the_year % 4) == 0 and (the_year % 100) != 0:
    print(the_year, "is a leap year.")
elif (the_year % 4) == 0 and (the_year % 100) == 0 and (the_year % 400) == 0:
    print(the_year, "is a leap year")
elif (the_year % 4) == 0 and (the_year % 100) == 0 and (the_year % 400) != 0:
        print(the_year, "is not a leap year.")

# part c)
print("part c)")
if (the_year % 4) == 0 or ((the_year % 100) == 0 and (the_year % 400) == 0):
    print(the_year, "is a leap year.")
else:
    print(the_year, "is not a leap year.")