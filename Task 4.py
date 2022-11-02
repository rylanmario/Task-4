# Name: Task 4.py
# Author: Rylan Fessey
# Date created: October 29th, 2022
# Date last modified: October 29th, 2022
# Purpose: The purpose of this program is to take user input on temperture or speed and convert to another format.


convertion = int(input("Would you like to convert speed or temperture? Type 1 for temperture or 2 for speed: "))

def temperture():
    tempConvert = int(input("Are you converting to celcius, or to farenhehit? Type 1 for Celcius or 2 for farenheit: "))
    if tempConvert == 1:
        tempC = int(input("What is the temperture you are converting from in Celsius?: "))
        cConvertion = (tempC * 9/5) + 32
        print(tempC, "in farenheit is", cConvertion, "")
    elif tempConvert == 2:
        tempF = int(input("What is the temperture in Farenheit?: "))
        fConvertion = (tempF - 32) * 5/9
        print(tempF, "in celcius is", fConvertion, "degrees celsius")
    else:
        print("Please enter a valid option. Valid options are 1 or 2.")

def speed():
    speedConvert = int(input("Are you converting to Km/h or to Mph? Type 1 for Km/h or 2 for Mph.: "))
    if speedConvert == 1:
        speedKPH = int(input("What is the speed in kilometers?: "))
        KPHConvert = speedKPH / 1.609
        print(speedKPH, "in miles is", KPHConvert, "MPH")
    elif speedConvert == 2:
        speedMPH = int(input("What is the speed in miles?: "))
        MPHConvert = speedMPH * 1.609
        print(speedMPH, "in kilometers is", MPHConvert, "Km/h.")

if convertion == 1:
    temperture()

elif convertion == 2:
    speed()

else: 
    print("Please choose a valid option. Valid options are 1 or 2.")


input("Press enter to exit:")
exit()
