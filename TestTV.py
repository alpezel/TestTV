#### make display menu later ####
def display_menu():
    print ("\n\033[0;39m===================================================")
    print ("                    TV SWITCH                      ")
    print ("===================================================")
    print ("\n     1. ON")
    print ("     2. OFF")
    print ("     3. SET CHANNEL")
    print ("     4. CHANNEL UP")
    print ("     5. CHANNEL DOWN")
    print ("     6. SET VOLUME")
    print ("     7. VOLUME UP")
    print ("     8. VOLUME DOWN")
    print ("\n===================================================")

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

    
    def setChannel(channel: 1): None

    def getVolume():
        volumenow= 1
        
        return
        

    def setVolume(volumelevel: int):
        volume_num = int(input("What Volume Level you want? "))
        if volume_num in volume_lvl:
            print("Volume Level: ", volume_num)
        else:
            print("The volume is only up to 7")
        return


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
TV.turnOff()
while True:
    display_menu()
    while True:
        try:
            button = int(input("Press the number you want to operate "))
            if button < 7 and button >= 1:
                break
        except ValueError:
            print("The input is not in the menu")
        else:  
            print("The input is not in the menu")
    
    if button == 1:
        print("\nTURNING ON...\n")
        TV.turnOn()
    elif button == 2:
        print("\nTURNING OFF...\n")
        TV.turnOff()
        break
    elif button == 3:
        TV.setChannel()
    elif button == 4:
        TV.channelUp()
    elif button == 5:
        TV.channelDown()
    elif button == 6:
        TV.setVolume()
    elif button == 7:
        TV.volumeUp()
    elif button == 6:
        TV.volumeDown()
    