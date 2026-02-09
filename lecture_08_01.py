# This file is for chapter/lecture 8 in the series. The broad topic of this chapter is top-down
# design of a program. This method of programming takes a end goal and breaks it down into
# smaller tasks. Each smaller task can then be broken down into an even smaller task. This can
# happen repeatedly until the task is small enough that it can be written as one line of code.
# This happens for each task. Once it is done for all of the tasks, ideally, the whole program can
# be written. I am sure the real process and results end up different.

# For this stage of the chapter in the PDF, the idea is to get a file of data to read from a
# weather website and analyze it. The rest below describes the program once you have the file and
# how to process the file to get the information from it and present it. The information below is
# more on how that process is presented.
# Here is an example of three lines of the file:
# 1/1/2000,79,37,0
# 1/2/2000,79,68,0
# 1/3/2000,73,50,0

# The following is the top down approach to dealing with the goal of reading in the file and
# processing the data into the program. The hastag formatting is to separate it from the code.
# The other two goals of the program are listed after the first breakdown of tasks of reading
# in the data: Analyze Data and Present Results
# AS THE PROGRAM PROGRESSES, EACH SECTION WILL LIKELY BE COMMENTED OUT AND THE NEXT SECTION WILL
# HAVE THE LATEST CODE.

########## Read in Data ##########
# Open File
# Read lines from file
# Close file
########## Analyze Data ##########
########## Present Results ##########

# Above is the first part of the process of writing the code in the IDE or text editor used. Below,
# is the rest of the program but it is presented in steps for each sub-task presented above. But
# it will be written below as if it were all at once. Now, the CSV file must be produced from
# a site that provides weather data so there is a file to read. I could make one up but I might as
# well do it the way described for fun. I could write a program to produce random temperatures.
# After finding a website to give me data on temperatures for New Glasgow, NS, I can only get them
# as far back as July 9, 2025 from that particular site:
# https://newglasgow.weatherstats.ca/charts/temperature-daily.html
# I am going to use the month of August. And I am changing the data to be read to what I can get
# from that site: Date, Max Temp, Hourly Mean Temp, Mean of Min/MAx Temp, Min Temp

"""
########## Read in Data ##########
# Open File
filename = input("Enter name of the data file: ")
infile = open(filename, 'r')
# These next two lines were not included but I did it just to be particular.
# After running the code, I see that it does not print the text in the CSV file. It prints
# something to tell you how the file is processed by Python 3. See below for the output:
# <_io.TextIOWrapper name='New_Glasgow_Temperatures_August_2025.csv' mode='r' encoding='UTF-8'>
print(infile)
infile.close()
# Read lines from file
# Close file
########## Analyze Data ##########
########## Present Results ##########
"""

# THERE IS REALLY TOO MUCH MATERIAL TO PROVIDE ALL OF THE MATERIAL AS PROVIDED IN THE PDF. JUST
# GO BACK AND READ THE PDF TO GET EVERYTHING. BUT FOR DEMO PURPOSES OF HOW THIS CHAPTER PROGRESSES,
# HERE IS THE NEXT SECTION

"""
########## Read in Data ########## #Open File
filename = input("Enter the name of the data file: ")
infile = open(filename, 'r')
#Read lines from File
datalist = []
for line in infile:
    #get data from line
    #Put data into list
#Close File
########## Analyze Data ##########
########## Present Results ##########
"""

# My first thought when looking at the above pseudo-code is to read each line of the file and make
# that line a string. Each new line read would become an element in the list called datalist[]
########## Read in Data ########## #Open File
filename = input("Enter the name of the data file: ")
# At this point, the filename is too long. I am shortening it to temps.csv
infile = open(filename, 'r')
#Read lines from File
datalist = []
for line in infile:
    #get data from line
    date, maxt, meant, mean_min_max, mint = line.split(',')
    """
    I made a mistake with the processing of the line read from the file. The PDF shows the use of
    integers in the lines of the file. I got my numbers from the web and ended up with floating
    point numbers with 3 digits, two magnitudes of order on the left side (whole number), and one
    order of magnitude to the right of the decimal point. I was trying to cast the resulting
    # number using int which caused a problem. However, it made me work on processing the resulting
    # variable to get rid of the newline character that showed up when the error was shown after
    # running the program. I got that part of the code to work in the end but only once I processed
    # the variable as a float. I did get rid of the newline character though, so I am including
    # that code in this comment.
    # print(line) # error for cast to int for mint, it has a newline character at the end, process it
    # for now call process mint ==> temp_lowtemp
    count = 0
    for digit in mint:
        print("digit: ", digit)
        count += 1
    print("count: ", count)
    # Between printing the line and the above loop, I get a character count and can see that there
    # is a newline character, \n, at the end of mint. The newline character only counts as one
    # character even though you can count mint in the error as 6 characters. I will have to
    # experiment with slicing the string to process it to get rid of the newline.
    temp_lowtemp = mint[0:5]
    print("temp_lowtemp: ", temp_lowtemp)
    lowtemp = float(temp_lowtemp)
    """
    # NEW PROBLEM - after processing the spreadsheet file to get an working date format, it
    # changed all the temperatures to use a symbol for degrees and a C with a space before the
    # degree symbol. Rather than process the spreadsheet again, I will adapt the code in the
    # comment above to get rid of those extra characters and give me floats.
    # Actually, I started to write the loop and then realized that I can slice the variable like
    # it is an list of characters, just like any list.
    lowtemp = float(mint[0:3])
    hightemp = float(maxt[0:3])
    avg_temp = float(meant[0:3])
    avg_min_max_temp = float(mean_min_max[0:3])
    # The PDF shows the use of a / as the delimiter for the date. My file uses a -.
    # And I changed the order of the date to work with the output that my spreadsheet app does
    y, m, d = date.split("-")
    year = int(y)
    month = int(m)
    day = int(d)
    #Put data into list
    datalist.append([day, month, year, lowtemp, hightemp, avg_temp, avg_min_max_temp])
    print(datalist)
#Close File
# This is the simple command on the line below
infile.close()
########## Analyze Data ##########
# The content continues on from here with something simple and probably will not require changing
# the code above. However, that may prove to be different as I continue to work through it. It
# could be that I need to change something above because I did something different that what is
# presented in the PDF. Or there could be another reason.

# Get date of interest
month = int(input("For the date you care about, enter the month (1 - 12): "))
day = int(input("For the date you care about, enter the day (1 - 31): "))
# The year is not needed as they are all from 2025 this time.
# Find historical data for date
gooddata = []
for single_day in datalist:
    #print("single_day: ", single_day)
    if(single_day[0] == day) and (single_day[1] == month):
        gooddata.append([single_day[3],
                         single_day[4], single_day[5]])
"""single_day[0], single_day[1], single_day[2],"""
print("gooddata: ", gooddata)
# Perform analysis
min_so_far = 100        # Setting a value higher than the expected minimum temperature ensures
                        # the value to change. The same is true in the opposite way for the max
max_so_far = -100
num_good_dates = 0
sum_of_min = 0
sum_of_max = 0
sum_of_avg = 0
for single_day in gooddata:
    num_good_dates += 1
    sum_of_min += single_day[0]
    sum_of_max += single_day[1]
    sum_of_avg += single_day[2]
    if single_day[0] < min_so_far:
        print("min_so_far: ", min_so_far, single_day[0])
        min_so_far = single_day[0]
    if single_day[1] > max_so_far:
        max_so_far > single_day[1]
avg_low = sum_of_min / num_good_dates
avg_high = sum_of_max / num_good_dates
########## Present Results ##########
"""
In the PDF it talks about presenting the results. It says that it will look at giving the output.
It says it will print out the highest and lowest and then the average low and high. However, the
information processed at this point is not actually anything other than the information for one
day. That is not really an average, just being for one day, unless the number is an average itself.
I think they just wanted to demonstrate that code was written to represent the larger process that
would normally be done to process data.
"""
print("There were ", num_good_dates, " days")
print("The lowest temperature on record was ", min_so_far, " degrees C")
print("The highest temperature on record was ", max_so_far, " degrees C")
print("The average low has been ", avg_low, " degrees C")
print("The average high has been ", avg_high, " degrees C")