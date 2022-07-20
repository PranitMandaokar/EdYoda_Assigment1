
series = [5,10,15,20,25,30,35,40,45,50]  # given series

print("numbers : ",series)          # to print the series

e = 0
o = 0

for i in series:                          # logic to get even and odd number 
    if i % 2 == 0:
        e += 1
    else:
        o += 1

print("Number of Even numbers :",e)    #to print the number of even and odd number
print("Number of Odd numbers :",o)