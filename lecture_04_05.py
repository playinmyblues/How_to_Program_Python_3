# This version makes a couple more improvements over the previously provided version. It
# prompts the user to put in a positive value for a payment and prompts again if needed. But if the
# user still puts in a 0 or less value, it assigns a value of 1.

# Get info from user - this is what is presented, not how I might write my own version
print("I'll help you determine how long you need to save.")
name = input("What is your name? ")
item = input("What is it you are saving up for? ")
# concatenating strings to form one variable for input argument
name_n_cost_question = "OK " + name + ". Please enter the cost of the " + item + ": "
balance = float(input(name_n_cost_question))
if (balance < 0):
    print("Looks like you have already saved enough.")
    balance = 0
    payment = 1
else:
    payment = float(input("Enter how much you will save each period: "))
    if(payment <= 0):
        payment = float(input("Savings much be positive. Please enter a positive value: "))
        if(payment <= 0):
            print(name, """, you still did not enter in a positive number! I am just going to 
                        assume you save 1 per period.""")
            payment = 1
# Calculate number of payments that will be needed
num_remaining_payments = balance/payment
# Present information to user
print(name + ", you must make", num_remaining_payments, "more payments, and then you will have your", item + "!")

# Then you test the program to make sure it works for all cases it was desgiened for. In the process,
# you might discover an area that could be improved upon. Then you write the next iteration to
# make improvements.