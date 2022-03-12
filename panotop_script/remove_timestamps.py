"""
    Simple formatting script that takes input from Panotop lecture notes
    and removes the timestamps - shortens the number of lines in the file
"""

import sys
import re
from unittest import skip

timestampRegex = "([0-9]:)?[0-9]+:[0-9][0-9]"

file_path = sys.argv[1]
print("Operating on " + str(file_path))

in_file = open(str(file_path), "r")
out_file = open(str(file_path)[:len(str(file_path))-4] + "_new.txt", "x")

lines = in_file.readlines()

for line in lines:
    if not re.match(timestampRegex, line):
        out_file.write(line)
