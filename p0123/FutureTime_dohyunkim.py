#FutureTime.py
#Name: Dohyun Kim
#Date: 2020-01-23
#Assignment: FutureTime

# datetime will allow us to access the system date and time.
import datetime

def main():
    #getting current time from system, storing to variable
    now =datetime.datetime.now()
    currentHour = now.hour
    currentMinute = now.minute

    print (str(currentHour) ,": ", str(currentMinute)) #this is just for checking, we should delete it later

    userHour = int(input("input Hour : "))
    userMinutes = int(input("input minutes : "))

    resultMinutes = userMinutes+currentMinute
    tmpHour,resultMinutes = divmod(resultMinutes, 60)
    resultHour=  (userHour+currentHour +tmpHour)%12


    print( "result => " , resultHour ,":", resultMinutes )

    #TODO:
    #Ask user for hours
    #Ask user for minutes

    #Calculate the time after the user-supplied time has passed.

    #Do not use any if statements in calculating the time.

    #Output the future time in standard format "HH:MM"


main()