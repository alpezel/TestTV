# this is where the tv1 and tv2 are
from TV import TV

def main():
    tv1 = TV()
    tv2 = TV()

    
    print("tv1's channel is ",tv1.get_channel(),"and volume level is",tv1.get_volume())
    tv1.turn_on()
    tv1.set_channel(30)
    tv1.set_volume(3)
    print("tv1's channel is ",tv1.get_channel(),"and volume level is",tv1.get_volume())

    print("tv2's channel is ",tv2.get_volume(),"and volume level is",tv2.get_volume())
    tv2.turn_on()
    tv2.set_channel(3)
    tv2.set_volume(2)

print("this is a test")
main()