from enum import Enum

class Climate(Enum):
    TROPICS = 1
    MID_LATITUDE_SUMMER = 2
    MID_LATITUDE_WINTER = 3
    COLD_ZONE_SUMMER = 4
    NONE_TYPE = 5

def getDetermination(type):
    if (type == Climate.TROPICS):
        return (0.95, 0.98, 1.02)
    elif (type == Climate.MID_LATITUDE_SUMMER):
        return (0.97, 0.99, 1.02)
    elif (type == Climate.MID_LATITUDE_WINTER):
        return (1.03, 1.01, 1.00)
    elif (type == Climate.COLD_ZONE_SUMMER):
        return (0.99, 0.99, 1.01)
    else:
        raise ("Climate type no found.")
