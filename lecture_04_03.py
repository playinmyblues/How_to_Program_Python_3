# This program explores the concepts for chapter 4. Chapter 4 is about developing programs. It
# covers three ideas: 1) plan ahead, 2) keep on testing, and 3) develop iteratively (pyramid style)

# Each iteration is numnered in sequence. New code is added each time.

# We still must test other conditions to make sure they allow the program the work or crash it.
# We can test for a 0 balance and positive payment which works. Another situation is to enter in a
# positive balance but a negative payment. Another situation is a negative balance and a positive
# payment. Both of this result in a negative number of payments. While that can make sense if we
# were writing a banking program, it does not work for one that helps you save money that goes
# towards a specific goal.

# Let us treat the negative payment case as information that means enough money has already been
# saved. The addition of code here will be written to account for that specific condition. It is
# written above, just after the code accepting the first user input. TIME: 19:42

# Get information from user:
balance = float(input("Enter how much you want to save: "))

# This new code deals with both a 0 balance and if a 0 payment is entered - but not with a loop
if (balance < 0):
    print("It looks like you already saved enough!")
    balance = 0
    payment = 1
else:
    payment = float(input("Enter how much you will save each period: "))
    if(payment <= 0):
        payment = float(input("Savings must be positive. Please enter in a positive value: "))

# Testing line 1:
print("Balance is", balance, "and payment is", payment)

# Now to calculate the number of payments that will be needed
num_remaining_payments = balance/payment

# Now, present information to user
print("You must make", num_remaining_payments, "more payments.")