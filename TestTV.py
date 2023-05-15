# Make a Class named TV
class TV:
    # Create 2 objects 
    def __init__(tv_object, channel, volume ):
        tv_object.channel = channel
        tv_object.volume = volume

    # Add methods and define
    def turnOn():
        print("The TV is ON")
     
    def turnOff():
        print("The TV is OFF")
    
    def getChannel():
        for i in (channel):
            channel_num[i] = channel_num[i] -1 
            return channel_num                      

    
    def setChannel(channel: int): None

    def getVolume(): int

    def setVolume(volumelevel: int): None

    def channelUp():None

    def channelDown():None

    def volumeUp():None

    def volumeDown():None

    
channel = list(range(1,121))
volume = list(range(1,8))
print("The current channel (1 to 120) of this TV.")
print("The current volume level (1 to 7) of this TV.")
TV.turnOff()
while True:
    switch = input("Do you want to turn on your TV? ")
    while switch.lower()!= "yes" and switch.lower() != "no":
        print ("\n[The input is not (yes or no)]\n")
        switch = input("Do you want to turn on your TV? ")
    # Indicates whether this TV is on/off
    if switch.lower() == "yes":
        TV.turnOn()
        channel_num = int(input("What channel number you want? "))
        TV.getChannel()
    elif switch.lower() == "no":
        TV.turnOff()
        break


    


