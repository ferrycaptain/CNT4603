__author__ = 'Brian M Batinchok' \
             'CNT4603 Spring 2015' \
             'zipcode.py'
# Script to Validate US ZipCodes

import sys,os,csv,re

# Prompt User for File Input
userInput = input("Please Enter the name of the file containing the input ZipCodes: \n")
# Open the filename in read mode provided by User
fileObject = open(userInput, 'r')
# Read File and save to variable allLines
allLines = fileObject.readlines()
# Close File
fileObject.close()
# Loop through eachLine of allLines
for eachLine in allLines:
    # Check for pattern
    pattern = '(\d{5}(-\d{4})?$)'
    # If found flag M
    m = re.search(pattern, eachLine)
    # Print to User
    if m is not None:
        print("Match Found - Valid US ZipCode: ", eachLine, "\n")
    else: print("Error - no match with: ", eachLine, "\n")
