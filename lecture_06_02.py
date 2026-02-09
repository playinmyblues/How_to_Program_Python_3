# This is the second Python file covering material from Lecture 6. The material covered starts
# at 14:57 (mm:ss). The current material at the beginning of this section is reading lines from
# a text file.

# The next section shows how to read a line from a text file, one line, and then prints it out, just
# to confirm that the process worked.
myfile = open("results.txt", "r")
line_from_file = myfile.readline()
myfile.close()
print(line_from_file)

# The above process reads only one line. To read a second line, the process requires a second
# realine() command - easy enough to do. See below. Note that the assignment statement still occurs
# because the file has been closed in the previous block of code.
myfile = open("results.txt", "r")
line_from_file1 = myfile.readline()
line_from_file2 = myfile.readline()
myfile.close()
print(line_from_file1)
print(line_from_file2)

# The next step in the video shows the opening of a second file to be the output file. It is done
# immediately after opening the input file, the file from which the lines are read. But I think
# it will work just fine to do the output file later as the required lines are assigned to string
# variables. That might change if the situation for reading and writing were different.
myfile = open("results.txt", "r")
line_from_file1 = myfile.readline()
line_from_file2 = myfile.readline()
myfile.close()
outfile = open("lecture02_outfile.txt", "w")
outfile.write(line_from_file1)
outfile.write(line_from_file2)
# Check the outfile in the directory for verification. After writing the code, I think that it
# the code is presented in the video as it is to keep ideas together and code together.

# The next block of code shows how to read a line from a text file that has a number. But the
# number in a text file is still taken in as a string so it must be cast as a float.
infile = open("file_with_numbers.txt", "r")
line_from_file = infile.readline()
speed = float(line_from_file)
print("Speed: ", speed, "Speed x 10 = ", speed * 10)
infile.close()

# This next block of code shows how to read multiple lines of a file and stop reading when the
# last line of the file is read. When the last line is read, it attempts to read the next line and
# comes to the end of the file, an empty string is returned.
myfile = open("results.txt", "r")
line_from_file = myfile.readline() # this line is required before the while condition is tested
i = 1
print("line", i, "contains:", line_from_file)
while line_from_file != "":
    i += 1
    print("reading next line,", i)
    line_from_file = myfile.readline()
    print("line", i, "contains:", line_from_file)
    # This is not perfect in terms of the loop providing feedback on exactly what is going on
    # but it can be interpreted that the empty content on the last printed info shows the end
myfile.close()

# The next block shows how to do a similar thing with a for loop. For loops in Python3 can be
# done in such a way that the loop advances without having to specify an increase in the counter
# and the counter is implicitly declared.
myfile = open("results.txt", "r")
j = 1
for line_from_file in myfile:
    print("line", j, "contains", line_from_file)
    j += 1
myfile.close()
# 19:00, mm:ss in lecture
