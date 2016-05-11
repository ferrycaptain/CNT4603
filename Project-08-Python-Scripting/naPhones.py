__author__ = 'Brian M Batinchok' \
             'CNT4603 Spring 2015' \
             'naphones.py'
#Script to Validate North American Phone Numbers

import sys,os,csv,re

# Prompt User for File Input
userInput = input("Please Enter the name of the file containing the input Phone Numbers: \n")
# Open the filename in read mode provided by User
fileObject = open(userInput, 'r')
# Read File and save to variable allLines
allLines = fileObject.readlines()
# Close File
fileObject.close()
# Loop through eachLine of allLines
for eachLine in allLines:
    # Check for pattern
    pattern = '([2-9]\d{2}[-\.\s]??[2-9]\d{2}[-\.\s]??\d{4}|\([2-9]\d{2}\)\s*\d{3}[-\.\s]??\d{4}' \
              '|[2-9]\d{2}[-\.\s]??\d{4})'
    # Flag M if pattern is valid
    m = re.search(pattern, eachLine)
    # Print Statements to User
    if m is not None:
        print("Match Found - Valid US Phone Number: ", eachLine, "\n")
    else: print("Error - no match with: ", eachLine, "\n")
