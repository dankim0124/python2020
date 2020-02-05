# WeatherApp.py
# Name: Dohyun Kim
# Date: 01/27
# Assignment: WeatherApp.py

from WeatherInfo import *

# Set your key
default_key = "78d0d89c19f6f82d4372e9c0a8177f44"
setKey(default_key)


def run():
    input_city = input("input your city : ")
    setCity(input_city)
    replay = None
    updateWeather()
    kelvin_temp = getTemp()
    wind_speed = getWindSpeed()

    fahrenheit = KelvinToFahr(kelvin_temp)
    wind_des = getWindDes(wind_speed)
    jacket = getProperCloth(fahrenheit)
    umbrella = "You should bring your umbrella" if isUmbrella(getDescription()) == 1 else ""
    print("The current weather in ", input_city, " is ", getDescription(), " with ", getHumidity(), "% humidity")
    print(umbrella, end='')
    print("Temperature : ", round(fahrenheit, 2), " degrees Fahrenheit")
    print("Wind speed : ", round(getWindSpeed(), 2), " - ", wind_des)
    print("you should wear a ", jacket, " today!\n")

    while replay != "Y" and replay != "N":
        replay = input("Would you like another weather report? (Y/N):")
        if replay != "Y" and replay != "N":
            print("input Y or N ")
    return replay


def KelvinToFahr(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


def getProperCloth(fh):
    if 55 <= fh < 65:
        return "light jacket"
    elif 40 <= fh < 54:
        return "medium jacket"
    elif fh < 40:
        return "heavy jacket"
    else:
        return -1


def isUmbrella(des):
    if des == "mist" or des == "light rain" or des == "rain" or des == "heavy rain":
        return 1
    else:
        return 0


def getWindDes(wind_speed):
    if wind_speed < 1:
        return "Calm"
    elif wind_speed < 3:
        return "light air"
    elif wind_speed < 7:
        return "light breez"
    elif wind_speed < 12:
        return "gentle breez"
    elif wind_speed < 18:
        return "Moderate breez"
    elif wind_speed < 24:
        return "Fresh breez"
    elif wind_speed < 31:
        return "Strong breez"
    elif wind_speed < 38:
        return "High breez"
    elif wind_speed < 46:
        return "Gale"
    elif wind_speed < 54:
        return "Strong gale"
    elif wind_speed < 63:
        return "Storm"
    elif wind_speed < 72:
        return "Violent storm"
    elif wind_speed < 72:
        return "light breez"
    elif wind_speed >= 73:
        return "Hurricane"

while run() == "Y":
    pass

print("Goodbye")
