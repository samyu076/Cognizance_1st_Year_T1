import math
import os
import random
import re
import sys

def timeConversion(s):
    # Write your code here
    hour = int(s[:2])  
    minute = s[3:5] 
    second = s[6:8] 
    period = s[8:]
    if period == 'AM':
        if hour == 12:  # 12 AM is 00 in 24-hour format
            hour = 0
    else:  # PM case
        if hour != 12:  # Add 12 to PM hours except for 12 PM
            hour += 12
    
    # Return formatted string in 24-hour format
    return f"{hour:02}:{minute}:{second}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
