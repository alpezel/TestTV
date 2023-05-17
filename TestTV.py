# this is where the tv1 and tv2 are
from TV import TV

def test():
    tv1 = TV()
    tv2 = TV()
    
    print ("\033[0;39m===================================================")
    tv1.turn_on()
    tv1.set_channel(30)
    tv1.set_volume(3)
    tv1.turn_off()
    print("\n\033[0;33mTV 1's channel is ",tv1.get_channel(),"and volume level is",tv1.get_volume(),"\n")
    
    tv2.turn_on()
    tv2.set_channel(3)
    tv2.set_volume(2)
    tv2.turn_off()
    print("\n\033[0;33mTV 2's channel is ",tv2.get_channel(),"and volume level is",tv2.get_volume(),"\n")
    print ("\033[0;39m===================================================")
    # try channel up and volume up
    print("\033[0;31m[try channel up and volume up]")
    tv1.turn_on()
    tv1.channel_up()
    tv1.volume_up()
    tv1.turn_off()
    print("\n\033[0;33mTV 1's channel is ",tv1.get_channel(),"and volume level is",tv1.get_volume(),"\n")
    
    # try channel down and volume down
    print("\033[0;31m[try channel down and volume down]")
    tv2.turn_on()
    tv2.channel_down()
    tv2.volume_down()
    tv2.turn_off()
    print("\n\033[0;33mTV 2's channel is ",tv2.get_channel(),"and volume level is",tv2.get_volume(),"\n")
    print ("\033[0;39m===================================================")
test()