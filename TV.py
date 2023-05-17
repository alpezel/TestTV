    # Make a Class named TV
class TV:
    # Create 2 objects 
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.on = False

    # Add methods and define
    def turnOn():
        self.on = True
     
    def turnOff():
        self.on = False
    
    def getChannel(self):
        return self.channel
    
    def setChannel(self, channel):
        if 1 <= channel <= 120:
            self.channel = channel

    def getVolume(self):
        return self.volume
    
    def setVolume(self, volume):
        if 1 <= volume <= 7:
            self.volume = volume
     
    def channelUp(self):
        if self.on and self.channel < 120:
            self.channel += 1


    def channelDown(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    def volumeUp(self):
        if self.on and self.volume < 7:
            self.volume += 1
       
    def volumeDown(self):
        if self.on and self.volume > 1:
            self.volume -= 1

