# This program explores the concepts for chapter 4. Chapter 4 is about developing programs. It
# covers three ideas: 1) plan ahead, 2) keep on testing, and 3) develop iteratively (pyramid style)

# This version is a continuation of the program development. It is done this way to make it easier
# to read and understand the concepts presented and how they are implimented.

# Get information from user:
balance = float(input("Enter how much you want to save: "))
payment = float(input("Enter how much you will save each period: "))

# Here is new code to account for a negative balance meaning no more money needs to be saved
if (balance < 0):
    print("It looks like you already saved enough!")
    balance = 0

# The next step is to adjust the code provided before to account for negative payments, which also
# indicate no more money needs to be saved.

if(payment == 0):
    payment = float(input("$0 is not a valid input. Please enter a number greater than 0: "))
# While this above code is instructive for the user of the program, it does not prevent the user
# from entering 0 again. 0 will crash the program. LATER in the course, loops will be covered. A
# loop can help take care of this situation to keep prompting the user for a number greater than 0.

# Testing line 1:
print("Balance is", balance, "and payment is", payment)

# Now to calculate the number of payments that will be needed
num_remaining_payments = balance/payment

# Now, present information to user
print("You must make", num_remaining_payments, "more payments.")

# We still must test other conditions to make sure they allow the program the work or crash it.
# We can test for a 0 balance and positive payment which works. Another situation is to enter in a
# positive balance but a negative payment. Another situation is a negative balance and a positive
# payment. Both of this result in a negative number of payments. While that can make sense if we
# were writing a banking program, it does not work for one that helps you save money that goes
# towards a specific goal.

# Let us treat the negative payment case as information that means enough money has already been
# saved. The addition of code here will be written to account for that specific condition. It is
# written above, just after the code accepting the first user input.