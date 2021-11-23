first_number = input ("Enter a number : ")
second_number = input ("Enter a second number : ")
a = float (first_number)
b = float (second_number)
if a>10 and b>10:
    print ("Both numbers are greater than 10.")
elif a>10 and b<10:
    print ("One number is greater than 10, and one is smaler")
elif a<10 and b>10:
    print ("One number is greater than 10, and one is smaler")
else :
    print ("Both numbers are smaller than 10.")
