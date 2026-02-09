# This program explores the concepts for chapter 4. Chapter 4 is about developing programs. It
# covers three ideas: 1) plan ahead, 2) keep on testing, and 3) develop iteratively (pyramid style)

# The idea for this chapter is going to be a savings program. Its goals will be to help you:
# a) save money towards a goal
# b) set aside a certain amount every week or month
# c) program will tell you how many times you have to set aside that amount to meet the savings
# goal

# One of the main tools used to develop software is planning how the code will work. For this
# program, there are three main steps: a) get information from the user, b) calculate the number
# of payments that will be needed, and c) present information to the user.

# Get information from user:
balance = float(input("Enter how much you want to save: "))
payment = float(input("Enter how much you will save each period: "))
# This next line of code was written after the line where is says TIME: 15:45
if(payment == 0):
    payment = float(input("$0 is not a valid input. Please enter a number greater than 0: "))

# At this point, the next step is not to write the next bit of code. The next step is to test the
# code that has already been written. Testing can be done line-by-line or a more reasonable way
# might be to test by logical section. I can see a problem with the above code but I am going to
# go through with what the lecture does anyway. (The problem is that data entered in using the
# input() command results in that data being strings. To perform math, we need numbers.)

# Testing line 1:
print("Balance is", balance, "and payment is", payment)
# Video Time: 11:04
# Now to calculate the number of payments that will be needed
num_remaining_payments = balance/payment
# The error that results from the above code (the previous error provided as an example in the
# video was a mistyped variable name) is that the code tries to use two str types with a math
# operator, which will not work. So, the inputs must be converted to floats in the above code.

# Now, present information to user
print("You must make", num_remaining_payments, "more payments.")

# This works but we must run more tests to make sure it all works as needed. The standard inputs
# work well enough. But what happens when the payment entered is 0? This results in a divide by
# 0 in math. This produces an error. We need to account for this type of input so the program does
# not crash. TIME: 15:45
# At this point, let us use a simple case of using an if statement to test for a zero amount

# At this point, to add clarity, I am starting a new file with the more current information. That
# way, I do not have to keep adding in little notes about what came before and what note relates
# to which particular piece of code in such a way that the reader or myself, can easily understand
# the comments. There is too much information beyond this point.