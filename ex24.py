number = 7
color = "blue"
ae = input ("Guess a number between 1 and 20. ")
b = input ("Guess a color. ")
a = float(ae)
if a==7 and b=="blue" :
    print ("Bravo, both are correct!")
elif a==7 or b=="blue" :
    print ("One of both is correct!")
else :
    print ("Better luck next time.")

print ("Try again")