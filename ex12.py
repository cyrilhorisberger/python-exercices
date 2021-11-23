user_input = input ("How many dollars do you want to convert to swiss francs ? ")
dollars = float (user_input)
print (dollars)

def conv (dollars) :
    msg1 = " dollars are "
    msg2 = " swiss francs."
    result = dollars * 1.09
    phrase = str(dollars) + msg1 + str(result) + msg2
    return phrase

print (conv(dollars))

if float (user_input) >= 200:
    print ("That's a lot of money")