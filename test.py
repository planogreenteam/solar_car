import time
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

try: 
	ads = ADS.ADS1115(i2c)
except Exception as e: 
	print(e)

chan = AnalogIn(ads, ADS.P0, ADS.P1)
while True: 
	print(chan.value, chan.voltage)
	time.sleep(2)

