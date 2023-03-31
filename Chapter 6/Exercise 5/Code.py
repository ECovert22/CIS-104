text = "X-DSPAM-Confidence:    0.8475"

start = text.find(":") + 1  
num = text[start:].strip()  
print(float(num))