#### make display menu later ####
# Make a Class named TV
class TV:
    # Create 2 objects 
    def __init__(self, channel, volume ):
        self.channel = channel
        self.volume = volume

    # Add methods and define
    def turnOn():
        print("The TV is ON")
     
    def turnOff():
        print("The TV is OFF")
    
    def getChannel():
        channel_num = int(input("What channel number you want? "))
        if channel_num in channel:
            print("You're on channel ", channel_num)
        else:
            print("The channel does not exist")  
        return                   

    
    def setChannel(channel: int): None

    def getVolume():
        volume_num = int(input("What Volume Level you want? "))
        if volume_num in volume_lvl:
            print("Volume Level: ", volume_num)
        else:
            print("The volume is only up to 7")
        return

    def setVolume(volumelevel: int): None

    def channelUp():None

    def channelDown():None

    def volumeUp(self,volume):
        if volume in volume_lvl:
            self.volume -= 1
        return self.volume

    def volumeDown(self,volume):
        if volume in volume_lvl:
            self.volume -= 1
        return self.volume

    
channel = list(range(1,121))
volume_lvl = list(range(1,8))
print("The current channel (1 to 120) of this TV.")
print("The current volume level (1 to 7) of this TV.")
#print(channel)
TV.turnOff()
while True:
    switch = input("Do you want to turn on your TV? ")
    while switch.lower()!= "yes" and switch.lower() != "no":
        print ("\n[The input is not (yes or no)]\n")
        switch = input("Do you want to turn on your TV? ")
    # Indicates whether this TV is on/off
    if switch.lower() == "yes":
        TV.turnOn()
        TV.getChannel()
        TV.getVolume()
        try_vol= input("up or down")
        if try_vol == "up":
            TV.volumeUp()
        else:
            TV.volumeDown()
    elif switch.lower() == "no":
        TV.turnOff()
        break


    


