import re

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
total = 0
count = 0
for line in fhand:
        line = line.rstrip()
        nums = re.findall('^New Revision: ([0-9]+)', line)
        if len(nums) > 0:
            total += int(nums[0])
            count += 1

if count > 0:
    avg = int(total / count)
    print(avg)
else:
    print("No matching lines found")