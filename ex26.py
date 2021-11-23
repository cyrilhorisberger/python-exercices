def get_result(answer):
    if answer == "a":
        return "true"
    elif answer == "b":
        return "false"
    else :
        return "NA"

print("Do you like programing?")
print("a. Yes")
print("b. No")
result = input("Enter a or b: ")


if (get_result (result) =="true"):
        print("Awesome! Programming is really fun!")
elif (get_result (result) =="false"):
        print("Hang in there! It's an acquired taste!")
else :
        print("Didn't get your answer...")