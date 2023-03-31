text = "pizza"
textLength = len(text)
length = len(text)-1
int = 0

while True:
    letter = text[length-int]
    int = int+1
    print(letter)
    if int == textLength:
        break