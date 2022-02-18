
# This line opens the txt file
log_file = open("um-server-01.txt")

# here we are declaring a function that loops over each line in the file strips any white space and prints each line that has is on Tuesday. Looks like day is being set equal to the the characters found between index 0 and 3 to be tested.
def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        # if day == "Tue":
        if day == "Mon":
            print(line)

# This is our function invoked with the file as the argument
sales_reports(log_file)
