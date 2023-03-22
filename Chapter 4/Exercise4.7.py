def computegrade(s):
    if s>1:
        return("Error, Score greater then 1")
    elif s>=0.9:
        return("A")
    elif s>=0.8:
        return("B")
    elif s>=0.7:
        return("C")
    elif s>=0.6:
        return("D")
    elif s>=0:
        return("F")
    else:
        return("Error, Score Less then 0")
    
score = input("Enter Score: ")

s =float(score)
print(computegrade(s))