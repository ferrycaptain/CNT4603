__author__ = 'Brian M Batinchok' \
             'CNT4603 Spring 2015' \
             'ipaddress.py'
#Script to Validate IP Addresses

import sys,os,csv,re

# Prompt User for File Input
userInput = input("Please Enter the name of the file containing the input IP Addresses: \n")
# Open the filename in read mode provided by User
fileObject = open(userInput, 'r')
# Read File and save to variable allLines
allLines = fileObject.readlines()
# Close File
fileObject.close()
# Loop through eachLine of allLines
for eachLine in allLines:
    # Check for pattern
    pattern = '([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$'
    # Flag M if pattern found
    m = re.search(pattern, eachLine)
    #Print to User
    if m is not None:
        print("Match Found - Valid IP Address: ", eachLine, "\n")
    else: print("Error - no match - invalid IP Address ", eachLine, "\n")