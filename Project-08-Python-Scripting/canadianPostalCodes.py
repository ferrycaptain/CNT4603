__author__ = 'Brian M Batinchok' \
             'CNT4603 Spring 2015' \
             'canadianpostalcodes.py'
#Script to Validate Canadian Postal Codes

import sys,os,csv,re

# Prompt User for File Input
userInput = input("Please Enter the name of the file containing the input Canadian Postal Codes: \n")
# Open the filename in read mode provided by User
fileObject = open(userInput, 'r')
# Read File and save to variable allLines
allLines = fileObject.readlines()
# Close File
fileObject.close()
# Loop through eachLine of allLines
for eachLine in allLines:
    # Check for pattern
    pattern = '([(A,B,C,E,G,H,J,K,L,M,N,P,R,S,T,V,X,Y,0-9][A-Z0-9]*2)'
    # Flag M if pattern found
    m = re.search(pattern, eachLine)
    # Print to User
    if m is not None:
        print("Match Found - Valid Canadian Address Eh': ", eachLine, "\n")
    else: print("Error - No match - invalid Canadian Address ", eachLine, "\n")
