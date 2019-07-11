import time
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
ads = ADS.ADS1115(i2c)



def updateCurrent():
    try:
        chan = AnalogIn(ads, ADS.P2, ADS.P3)
        #current = chan.voltage / (0.5 * 10 ** (-3))
        x = chan.voltage
        current = [x, 0.3968 * x ** 2 + 1.1796 * x + 0.0137]
        #current = x
        #chan2 = AnalogIn(ads, ADS.P0, ADS.P1)
        #current = chan2.voltage
        if current is not None:
            return current
    except Exception as e:
        #print(e)
        pass

