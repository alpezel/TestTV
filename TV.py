# Make a Class named TV
class TV:
    # Create 2 objects 
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.on = False
    # Add methods and define
    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        if 1 <= channel <= 120:
            self.channel = channel

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        if 1 <= volume <= 7:
            self.volume = volume

    def channel_up(self):
        if self.on and self.channel < 120:
            self.channel += 1

    def channel_down(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    def volume_up(self):
        if self.on and self.volume < 7:
            self.volume += 1

    def volume_down(self):
        if self.on and self.volume > 1:
            self.volume -= 1

class Test_TV:
    def test(self):
        tv1 = TV()
        tv2 = TV()

        print("The initial channel of tv is ", tv1.get_channel(), "and the initial volume level is ", tv1.get_volume())

test_tv= Test_TV()
test_tv.test()