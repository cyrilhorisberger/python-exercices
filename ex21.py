user_number1 = input ("Enter a first number : ")
user_number2 = input ("Enter a first number : ")
result = float(user_number2)-float(user_number1)

if result > 10 :
    print ("The result is bigger than 10.")
elif result > 0:
    print ("The result is bigger than 0 but smaller than 10.")
elif result == 0:
    print ("The result is 0.")
else :
    print ("The result is a negative number.")

print ("You can try again!")
