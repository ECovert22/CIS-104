name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hoursDict = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        hour = time.split(":")[0]
        hoursDict[hour] = hoursDict.get(hour, 0) + 1
        
sortedHours = sorted(hoursDict.items())
        
for hour, count in sortedHours:
    print(hour,count)