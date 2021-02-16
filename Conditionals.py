#Create a function that accepts 3 parameters and checks for
#equality between any two of them.

#Your function should return True if 2 or more of the parameters
#are equal, and false is none of them are equal to any of the others.

Weather = "Rain"
Temp = 35
Walk = "Off"

if Weather == "Rain" and Temp < 55 and Temp > 32:
    Walk = "On"

elif Weather == "Snow" and Temp > 25:
    Walk = "On"

else:
    Walk = "Off"
