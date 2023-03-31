
fname = input("Enter file name: ")
if fname == "":
    fname = "mbox-short.txt"
fh = open(fname)

for line in fh:
     print(line.upper(), end="")
