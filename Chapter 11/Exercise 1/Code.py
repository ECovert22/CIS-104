import re

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
expression = input("Enter a regular expression: ")
count = 0
for line in fhand:
    line = line.rstrip()
    if re.search(expression, line):
        count += 1

print(fname," had ", count, "lines that matched ", expression)