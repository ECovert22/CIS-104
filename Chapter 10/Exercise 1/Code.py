fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
addresses = {}

for line in fhand:
    if line.startswith('From '):
        email = line.split()[1]
        addresses[email] = addresses.get(email, 0) + 1
if addresses:
    most_messages = max(addresses, key=addresses.get)
    print(most_messages, addresses[most_messages])
