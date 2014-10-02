#Matthew Wadkin
#02/10/14
#

water_temp = float(input("Enter the temperature of the water: "))
if water_temp < 0:
    if water_temp < -273.5:
        print("That is impossible as it is lower than absolute 0")
    else:
        print("The water is frozen")
elif water_temp > 100:
    print("The water is boiling")
else:
    print("The water is liquid")

          
        
