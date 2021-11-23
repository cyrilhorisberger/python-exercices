celsius = input ("Please enter a temperature in degrees Celsius : ")
cel = float(celsius)
def conv(cel):
    return (cel*9/5+32)

print (str(celsius)+" degrees are " + str(conv(cel))+" degrees Farenheit.")