#https://github.com/karioja/vedirect/blob/master/vedirect.py
import os
import Adafruit_ADS1x15
import time
import vedirect
import thread
import csv
from ADSfruit_ADS1X15.ADS1115.analog_in import AnalogIn

adc = Adafruit_ADS1x15.ADS1115()
"""chan = AnalogIn(ads, ADS.P2, ADS.P3)"""

#ve = vedirect.vedirect("/dev/ttyUSB0", 1)

# Or create an ADS1015 ADC (12-bit) instance.
#adc = Adafruit_ADS1x15.ADS1015()

# Note you can change the I2C address from its default (0x48), and/or the I2C
# bus by passing in these optional parameters:
#adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 2/3

divider1ratio = 5.461233
divider2ratio = 12

voltageAux = 0.0
voltageMainMPPT = 0.0
voltageMainBackup = 0.0
vAux = 0.0
vMain = 0.0
vShunt = 0.0
vCurrent = 0.0
# def updateMPPTCallback(data):
# 	global voltageMainMPPT
# 	voltageMainMPPT = float(data["V"])/1000

# def callVE():
# 	ve.read_data_callback(updateMPPTCallback)
#
# try:
#    thread.start_new_thread(callVE,())
# except:
#    print "Error: unable to start thread"
def updateCurrentOut():
	global vshunt
	global vcurrent
	file = open("/data/current.csv", "a")
	writer = csv.writer(file)_
	while True: 
		try: 
			"""vShunt = chan.voltage"""
			vShunt = adc.read_adc_difference(3, gain=GAIN)
q		except Exception as e: 
			errfile = open('/error.txt')
			errfile.write(str(e))
			errfile.write("Error in reading")
			errfile.close()
		
		vCurrent = vShunt / (0.5 * 10 ** (-3))		

		writer.writerow([vShunt, vCurrent])
		
		time.sleep(0.5)	

file.close()

def updateVoltage():
	global vAux
	global voltageAux

	while True:
		try:
			vAux = adc.read_adc(0, gain=GAIN)
			#vMain = adc.read_adc(0, gain=GAIN)
		except Exception as e:
			print "error reading"
			print e

		voltageAux = divider1ratio*vAux*0.1875/1000
		# voltageMainBackup = divider2ratio*vMain*0.1875/1000

		# print "Main Voltage:"
		# print voltageMainMPPT

		if (voltageAux < 12.15):
			os.system('mpg123 /home/pi/cool-guy-club/lowAux.mp3 &')
			print("lowAux Called")
		# if (voltageMainBackup < 48.6 or voltageMainMPPT < 48.6):
		# 	os.system('mpg123 -q lowMain.mp3 &')
		print voltageAux

		time.sleep(5)

def getAuxV():
    global voltageAux
    return voltageAux
try:
    thread.start_new_thread(updateVoltage,())
except:
    print "Error: unable to start thread"
