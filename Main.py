from Location import Location
from Climate import Climate
import matplotlib.pyplot as plt
import numpy as np

def Time_Hour():
    plt.title('Changes in solar radiant energy during the day')
    plt.xlabel('Time')
    plt.ylabel('Solar radiant energy (In theory)')

    data = []
    for time in range(6, 19):
        data.append(Location(173, 23, 114, 0, time, Climate.TROPICS).getH_instant())
    plt.plot(range(6,19),data)
    plt.show()

def Time_Day():
    plt.title('Changes in solar radiant energy during a year')
    plt.xlabel('Time')
    plt.ylabel('Solar radiant energy (In theory)')

    data = []
    for time in range(10, 351, 10):
        if 90 < time < 270:
            data.append(Location(time, 43, 114, 0, 12, Climate.MID_LATITUDE_SUMMER).getH_instant())
        else:
            data.append(Location(time, 43, 114, 0, 12, Climate.MID_LATITUDE_WINTER).getH_instant())

    plt.plot(range(10, 351, 10), data)
    plt.show()

def Space_Latitude():
    plt.title('Solar radiant energy as a function of latitude')
    plt.xlabel('Latitude')
    plt.ylabel('Solar radiant energy (In theory)')

    data = []
    for latitude in range(1, 91,3):
        if latitude < 22.5:
            data.append(Location(79, latitude, 173, 0, 12, Climate.TROPICS).getH_instant())
        elif latitude < 66.5:
            data.append(Location(79, latitude, 173, 0, 12, Climate.MID_LATITUDE_SUMMER).getH_instant())
        else:
            data.append(Location(79, latitude, 173, 0, 12, Climate.COLD_ZONE_SUMMER).getH_instant())


    plt.plot(range(1,91,3), data)
    plt.show()

def Space_Height():
    plt.title('Solar radiant energy as a function of height')
    plt.xlabel('Height')
    plt.ylabel('Solar radiant energy (In theory)')

    data = []
    for height in range(0, 24):
        data.append(Location(173, 43, 114, height/10, 12, Climate.MID_LATITUDE_SUMMER).getH_instant())
    plt.plot(range(1, 2401, 100), data)
    plt.show()

if __name__ == '__main__':
    Space_Height()

