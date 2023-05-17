# this is where the tv1 and tv2 are
from TV import TV

def main():
    tv1 = TV()
    tv1.turnOn()
    tv1.getChannel(30)
    tv1.getVolume(3)
    print("tv1's channel is ",tv1.getChannel(),"and volume level is",tv1.getVolume())


    tv2 = TV()
    tv2.turnOn()
    tv2.getChannel(3)
    tv2.getVolume(2)
    print("tv1's channel is ",tv2.getVolume(),"and volume level is",tv2.getVolume())

main()