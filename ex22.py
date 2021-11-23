gender = input ("What is your gender ? ")
def greet (gender):
    if gender == "male":
        return ("Hello Sire! Welcome back.")
    elif gender == "female":
        return ("Hello Madam! Welcome back.")
    else :
        return ("Hello! Welcome back.")

print (greet(gender))