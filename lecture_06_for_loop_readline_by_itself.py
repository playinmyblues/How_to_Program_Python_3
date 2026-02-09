# This is a test to confirm that the code will work as expected and not relying on code
# that was previously contained in a block of code already written. The code below works as
# expected
myfile = open("results.txt", "r")
j = 1
for line_from_file in myfile:
    print("line", j, "contains", line_from_file)
    j += 1
myfile.close()