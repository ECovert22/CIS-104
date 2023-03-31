name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

sender = dict()
for lines in handle:
    if not lines.startswith('From:'): continue
    lines = lines.split()
    lines = lines[1]
    sender[lines] = sender.get(lines, 0) + 1
       

Bigcomment = None
Bignum = None
for comment, num in sender.items():
    if Bignum is None or num > Bignum:
        Bigcomment = comment
        Bignum = num
   
print(Bigcomment, Bignum)