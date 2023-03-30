total = 0
count = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        total = total + num
        count = count + 1
    except ValueError:
        print("Invalid input")
average = total/count
print(total, count, average)