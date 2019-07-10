import time
from datetime import datetime
import csv
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
ads = ADS.ADS1115(i2c)

#csvfile = open("currentdata.csv", "a+")
#csvwriter = csv.writer(csvfile)
#csvwriter.writerow(['Time', 'Voltage', 'Current'])

#file = open("currentdata.txt", "a+")


def updateCurrent(): 
	try: 
		# differential mode
		chan = AnalogIn(ads, ADS.P2, ADS.P3)
		current = chan.voltage / (0.5 * 10 ** (-3))
		#print(chan.voltage, current)
		#csvfile.writerow([str(datetime.datetime.now()), chan.voltage, current])
		#now = datetime.now()
		#time = now.strftime("%H:%M:%S")
		#file.write(time +  str(chan.voltage) + str(current))
		return current
	except Exception as e: 
		print(e)
#j = 0
#while j < 500: 
#	updateCurrent()
#	j += 1
#	time.sleep(2)

#csvfile.close()
#file.close()
