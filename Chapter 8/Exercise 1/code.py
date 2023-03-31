def chop(lst):
    del lst[0]
    del lst[-1]

def middle(lst):
    return lst[1:-1]


list = ["a", "b", "c", "d", "e", "f"]
chop(list)
print(list)
print(middle(list))