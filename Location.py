from Climate import Climate, getDetermination
from math import sin, cos, radians, exp

class Location():

    N = 0
    Latitude = 0
    Longitude = 0
    Height = 0
    ClimateType = Climate.NONE_TYPE
    Time = 0
    G_on = 0
    G_0 = 0
    G_cd = 0
    G_cb = 0

    CosOfZenithAngle = 0
    Permeance = 0

    def __init__(self, n, latitude, longitude, height, time, climateType):
        self.N = n
        self.Latitude = latitude
        self.Longitude = longitude
        self.Height = height
        self.ClimateType = climateType
        self.Time = time

        self.CosOfZenithAngle = self.getCosOfZenithAngle()
        self.Permeance = self.getPermeance()

        self.G_on = self.getG_on()
        self.G_0  = self.getG_0()
        self.G_cd = self.getG_cd()
        self.G_cb = self.getG_cb()

    def getDeclination(self):   #赤纬角
        return 23.45*sin(radians(360*(284+self.N)/365))

    def getSolarHourAngle(self):    #太阳时角
        return 15*(self.Time - 12)

    def getCosOfZenithAngle(self):   #太阳天顶角
        declination = self.getDeclination()
        solarHourAngle = self.getSolarHourAngle()
        latitude = self.Latitude
        return cos(radians(latitude)) * cos(radians(declination)) * cos(radians(solarHourAngle)) \
               + sin(radians(latitude)) * sin(radians(declination))

    def getPermeance(self):
        r = getDetermination(self.ClimateType)
        A = self.Height
        a0_ = 0.4237-0.00821*((6-A)**2)
        a1_ = 0.5055+0.00595*((6.5-A)**2)
        k_  = 0.2711+0.1858*((2.5-A)**2)
        a0 = r[0]*a0_
        a1 = r[1]*a1_
        k  = r[2]*k_

        return a0 + a1 * exp(-k / self.CosOfZenithAngle)

    def getG_on(self):
        G_SC = 1367 #太阳常数
        return G_SC*(1 + 0.033 * cos(radians(360 / 365 * self.N)))

    def getG_0(self):
        return self.G_on * self.CosOfZenithAngle

    def getG_cb(self):
        return self.G_0*self.Permeance

    def getG_cd(self):
        return self.getPermeance2()*self.G_0

    def getPermeance2(self):
        return 0.271-0.294*self.Permeance

    def getH_instant(self):
        return self.G_cb + self.G_cd

