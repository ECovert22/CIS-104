count = {}
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        if len(words) >2:
            email = words[1]
            domain = email.split('@')[1]
            count[domain] = count.get(domain, 0) + 1

print(count)