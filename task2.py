# Task 2
#Write a python program that prompts the user for the name of .csv file then reads and displays each line of the file as a Python list. Test your program on the 2 csv files that you generated in Task 1.

import csv

# reading boys names 
with open('lab10Boys.csv', 'r') as csvBoys:
    reader = csv.DictReader(csvBoys)
    for row in reader:
        print(row['First Name'], row['Count'])


# reading girls names
with open('lab10Girls.csv', 'r') as csvBoys:
   reader = csv.DictReader(csvBoys)
   for row in reader:
       print(row['First Name'], row['Count'])
