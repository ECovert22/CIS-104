list = []

while True:
    userInput = input("Enter a number:")
    if userInput == "done":
        break
    try:
        num = float(userInput)
    except:
        print("Not a Valid Number.")
        continue
    list.append(num)

if list[0] != None:
    print("Maximum is:", max(list))
    print("Minimum is:", min(list))
else:
    print("No Valid Numbers Inputed.")