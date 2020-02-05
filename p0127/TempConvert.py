#TempConvert.py
#Name:
#Date:
#Assignment:

import math

def main():
    print("")
    #Prompt the user for a Fahrenheit temperature
    F =int( input ("input Fahrenheit temperature : "))
    #Convert that temperature to celsius, rounding to 1 decimal percision
    C = round((F-32)*5/9, 1)
    #Output converted temperature.
    print("Fahrenheit : ", F," \t Celcious : ", C)
main()