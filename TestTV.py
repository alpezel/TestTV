# Make a Class named TV
class TV:
    # Create 2 objects 
    def __init__(tv_object, channel, volume ):
        tv_object.channel = channel
        tv_object.volume = volume

    # Add methods and define
    def turnOn():
        print("The TV is On")
     
    def turnOff():
        print("The TV is On")
    
    def getChannel1():int
    
    def setChannel1(channel: int): None

    def getVolume(): int

    def setVolume(volumelevel: int): None

    def channel1Up():None

    def channel1Down():None

    def volumeUp():None

    def volumeDown():None

while True:
    switch = input("Do you want to turn on your TV?")
    while switch.lower()!= "yes" and switch.lower() != "no":
        print ("\n[The input is not (yes or no)]")
        switch = input("Do you want to turn on your TV?")
        TV.turnOff() 
    if switch.lower() == "yes":
        TV.turnOn()
        break


    


