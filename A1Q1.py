# Write a Python program to get the Fibonacci series between 0 to 50



a = 1                # first element of the fibonacci series
b = 1                # second element of the series
i = 0

while i >= 0:
    if a > 50:
        break
    print(a,end=" ")
    sum = a + b
    a = b
    b = sum
    i += 1