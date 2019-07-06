import time
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
ads = ADS.ADS1115(i2c)


def updateCurrent(): 
	try: 
		# differential mode
		chan = AnalogIn(ads, ADS.P2, ADS.P3)
		file = open("currentdata.txt", "a+")
		file.write(chan.voltage)
		file.close()
	except Exception as e: 
		print e 

while True: 
	updateCurrent()
	time.sleep(1)


