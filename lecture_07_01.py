# This is the first file for working through the material presented for the 7th lecture. This
# lecture covers lists or as they are often known in other programming languages, arrays. The word
# array is used in Python but array refers to a type of list. Here is the definition for arrays:
# Python Arrays
# In Python, array is a collection of items stored at contiguous memory locations. The idea is to
# store multiple items of the same type together. Unlike Python lists (can store elements of mixed
# types), arrays must have all elements of same type. Having only homogeneous elements makes it
# memory-efficient.

# There are a couple of things to go through for this first topic. One is the information presented:
# The code below runs through the array with a for loop.
daily_high_temps = [83, 80, 73, 75, 79, 83, 86]

# With the loop below, the 7 in the range() of the for loop has the count start at 0 and go to 6
# That is 7 positions which is also the number of positions in the list. Note that the notation
# for the for loop is different from what would be found in C++
# In the previous chapter's work, I provided some code that counted number of lines in the file
# before it reached the end. Similarly written code would probably work for counting the length
# of the list above. However, there is an easier way to find the length of a list in Python. That
# is the len() command.
for i in range(7):
    print("daily high temps, day", str(i + 1), ":", daily_high_temps[i])

# See the len() command used below
print("The length of the daily_high_temps list is", len(daily_high_temps), "places.")
print("Below is what an array looks like when the array is printed with not formatting:")
print(daily_high_temps)

# The next bit of code sheds some light on how the Python for loop actually works. I am used to
# seeing the i in a for loop being using for the index value for the array. However, upon seeing
# the next bit of code, I see it differently. The code provided if given first. Note the brevity.
for i in daily_high_temps:
    print(i)
# Note that the output is simply the values contained in the list. i is assigned the value in the
# list each time the loop executes. It is not assigned the index value. To verify, I can use a
# different variable name in place of i and it will do the same thing.
print("Next example")
for the_array_value in daily_high_temps:
    print(the_array_value)

# To change a value in the array, use the array name and index as shown below and an assignment
print("Changing a list value")
daily_high_temps[2] = 101
print(daily_high_temps)

# Appending to lists is another option. You can append a single value as well as append one list
# to another list. Appending lists by using the .append() command can be useful when unknown
# numbers of values need to be appended to a list
list_1 = [1.1, 3.3, 5.5, 2.2, 6.6, 4.4]
value_to_be_appended = 44.4
list_2 = [9.9, 10.1, 11.1, 13.3, 12.2]
list_1.append(value_to_be_appended)
# Appending to a list by appending another list:
list_3 = list_1 + list_2
print("list_3:", list_3)

# You can also use the commonly used math oeprations in this case: +=. And then, the same list
# name can be used again, although, the same list name could be used again above.
list_1 = [1.1, 3.3, 5.5, 2.2, 6.6, 4.4]
list_2 = [9.9, 10.1, 11.1, 13.3, 12.2]
list_1 += list_2
print("list_1:", list_1)
# Page 73 of PDF
# Indexing of lists - this topic is interesting as providing an index value above the last index
# value of the list will throw an error. An index value of 7 or above will throw and error. How-
# ever, a -1 will allow you to access the last item of the list.
print("last value of list_3:", list_3[-1])
# What about -2
print("using -2 as index value:", list_3[-2])
print("using -3 as index value:", list_3[-3])
print("using -12 as index value:", list_3[-12])
# Now to use an index value -2 beyond the number of negative number of indices
# print("using -13 as index value:", list_3[-13]) # this causes an error