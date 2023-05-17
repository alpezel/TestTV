# this is where the tv1 and tv2 are
from TV import TV
def main():
    tv1 = TV(30,3)
    print("tv1's channel is ",tv1.getChannel,"and volume level is",tv1.getVolume)

    tv2 = TV(3,2)
    print("tv1's channel is ",tv2.getVolume,"and volume level is",tv2.getVolume)

main()