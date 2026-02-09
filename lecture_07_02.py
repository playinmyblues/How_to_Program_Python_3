# This file continues with material about lists. The first topic covered in this file is about
# slicing. Slicing allows you obtain a specific section of a list. But that can range from one
# element of the list to the whole list and any number of adjacent elements between. See below
from operator import truediv

this_list = [23, 45, 22, 12, 46, 99, 190, 1000, 900]
print(this_list)
# The first three elements, note that the number 3 indicates the index after the last item needed:
print("The 1st three elements:", this_list[0:3])
# elements 4 and 5 - can be assigned to a new variable
needed_slice = this_list[4:6]
print("Elements 4 and 5, AKA, the 5th and 6th items in the list:", needed_slice)
# Note the number before the colon is left out, indicating to start from the beginning of the list
print("The 1st 6 elements:", this_list[:6])
# Note the number after the colon is left out, indicates to go to the end of the list
print("From element 2 to the end:", this_list[2:])
# Using the negative notation within range to get the last elements from the list
print("Last 3 elements from the list:", this_list[-3:])
# I do not know why you would bother with this. Maybe they added this functionality with slicing
# a list to be consistent in providing all the options when developing it
print("Here is the whole list:", this_list[:])

# HERE IS SOMETHING PROVIDED IN THE PDF AND I WILL EXPLORE IT NOW RATHER THAT WAIT UNTIL LATER
# THERE IS NO EXAMPLE PROVIDED WITH THE INFORMATION BELOW:
# Slicing can let us do some interesting things. We can reassign values to slices, for example,
# replacing part of a list with another list. We can also insert some new values into the list.

# I will work on replacing items 0 to 2 in this_list
new_items = [999, 1111, 2222]
this_list[0:2] = new_items
# A quick test of simply running the file at this point shows something acceptable happened as no
# error was thrown. Now to print this_list to see what the result is
print("New version of this_list:", this_list)
# It worked as expected

# Next comes lists of lists. See the simple example below
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Take note that it is the 2nd element of the list that is printed, element at index 1
print("list_of_lists[1]:", list_of_lists[1])

# CHECK THIS OUT:
# Python lets you create lists in which you have a combination of different types. Most languages
# require an array to be all stuff of the same type, but in Python, it’s okay to have a list of
# items with an integer, a float, a string, and another list, for example. This is useful when you
# want to group unlike things together.
multi_format_list = [[1, 2, 3], ["one", "two", "three"], [1.0, 2.0, 3.0], [True, False, True]]
print("multi_format_list:", multi_format_list)
print("The above list of lists consists of integers, strings, floats, and boolean listerals.")
# Note that you can put a variable name in as part of the list. Let's try adding just an item
other_multi_list = [[23, 34, 45], multi_format_list]
print("other_multi_list:", other_multi_list)
other_multi_list.append(10011)
print("new other_multi_list:", other_multi_list)
# Note the way the list is printed. When working with such a list, it might be better to assign
# that one item to a list by itself. Otherwise, you might get stuck writing some extra code in the
# process of trying to deal with items in different ways.
new_list = [10011]
other_multi_list[-1:] = new_list
print("new other_multi_list:", other_multi_list)
print(other_multi_list[-1])
another_one_item_list = [20022]
other_multi_list[-2] = another_one_item_list
print("new other_multi_list", other_multi_list)
other_multi_list[-1] = new_list
print("new other_multi_list:", other_multi_list)
sec_new_list = [[30033], [40044]]
other_multi_list[-2:] = sec_new_list
print("new other_multi_list:", other_multi_list)
other_multi_list[-1:] = new_list
print("new other_multi_list:", other_multi_list)
other_multi_list[-2:-1] = new_list
print("new other_multi_list:", other_multi_list)
single_item_list = [50055]
other_multi_list[-2:-1] = single_item_list
print("new other_multi_list:", other_multi_list)
print("sec_new_list[0:1] :", sec_new_list[0:1])
other_multi_list[-2:-1] = sec_new_list[0:1]
print("new other_multi_list:", other_multi_list)
print("single_item_list[0:1] :", single_item_list[0:1])
# All of this experimentation is me trying to figure out why some elements are assigned as single
# elements by themselves versus others being assigned as a list with the list notation of []
# HERE, I want to see if am item that has been created as a list will be assigned as such
other_multi_list[-1:] = sec_new_list[-1:]
print("new other_multi_list[-1:] :", other_multi_list)
# It was.
list_of_single_list = [[2233]]
other_multi_list[-1:] = list_of_single_list
print("new other_multi_list:", other_multi_list)
# And if the item in a list is created as a list, it will be assigned to a spot in a list of lists
# as a list. I think I was just getting a little confused as I had created a couple of varaibles
# as a list, not a list of list(s). To access the value to be assigned, Python seems to be
# accessing the item in the list, not the list itself.. So, if the item is an integer, an integer
# is assigned. If it is a list, a list is assigned.
# Page 76 in PDF