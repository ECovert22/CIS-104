fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
lettersDict = {}
lettersList = []

for line in fhand:
    line = line.lower()
    for char in line:
        if char.isalpha():
            lettersDict[char] = lettersDict.get(char, 0) + 1
for letter, count in lettersDict.items():
    lettersList.append((count, letter))
lettersList.sort(reverse=True)

for count, letter in lettersList:
    print(letter, count)
