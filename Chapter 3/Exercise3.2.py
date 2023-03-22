try:
    hrs = input("Enter Hours:")
    h = float(hrs)
except:
    print('error, please enter numbers for your inputs')
    quit()
try:
    rate = input("Enter Rate:")
    r = float(rate)
except:
    print('error, please enter numbers for your inputs')
    quit()
GrossPay = float(0)
if h<=40: 
    GrossPay = h*r
else:
    GrossPay = 420 + (h - 40) * r * 1.5
print(GrossPay)
