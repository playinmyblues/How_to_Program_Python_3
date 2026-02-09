# This version deals with the case of the number of remaining payments often not being a whole
# number. There is more than one way to deal with this situation as there often is with any
# problem when writing code.

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
# Calculate number of payments that will be needed - this approach calculates the number of
# remaining payments, coverts the floating point number to an integer and then checks that number
# against the floating point number. If it is less, 1 is added to the integer. It is done this way
# because in reality, if you keep to the payment schedule, anything less will leave you short -
# when adhering to payments as entered.
num_remaining_payments = int(balance/payment)
if(num_remaining_payments < balance/payment):
    num_remaining_payments += 1
    # The above line is me shortening up the code to something I know works
# Present information to user
print(name + ", you must make", num_remaining_payments, "more payments, and then you will have your", item + "!")

# Then you test the program to make sure it works for all cases it was desgiened for. In the process,
# you might discover an area that could be improved upon. Then you write the next iteration to
# make improvements.

# KEY TAKEAWAYS from this lecture:
# 1) Plan ahead before you actually write code
# 2) Keep on testing
# 3) Develop interatively (pyramid style)