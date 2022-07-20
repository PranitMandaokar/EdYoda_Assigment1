# Write a Python program that accepts a word from the user and reverse it.

word = input("INPUT :")           #ask user to enter the string
b = ""
for i in range(len(word)):
    b = word[i] + b
print("OUTPUT :",b)                # to print the reverse of string
