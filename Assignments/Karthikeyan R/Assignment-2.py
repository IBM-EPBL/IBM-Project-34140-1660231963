import random

flag = 1

while(flag==1 and flag!=2):
    temp = random.uniform(-80,190)
    humid = random.uniform(0,100)
    if(temp>=45):
        print("Alert!!! Alarm ON!!! High temperature detected")
        print("Temperature value is: "+str(temp)+"° C")
        print("Humidity value is: "+str(humid))
        print("Press 1 to turn off the alarm \nPress 2 to quit the program: ")
        flag = int(input())
    else:
        print("Normal temperature monitoring: ")
        print("Temperature value is: "+str(temp)+"° C")
        print("Humidity value is: "+str(humid))
