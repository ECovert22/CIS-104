# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    colon = line.find(':')
    value = float(line[colon+1:].strip())
    total += value

print("Average spam confidence:", total/count)
