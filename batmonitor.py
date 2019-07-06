#https://github.com/karioja/vedirect/blob/master/vedirect.py
import os
import Adafruit_ADS1x15
import time
import vedirect
import thread

adc = Adafruit_ADS1x15.ADS1115()

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

divider1ratio = 3.3333
divider2ratio = 12

voltageAux = 0.0
voltageMainMPPT = 0.0
voltageMainBackup = 0.0
vAux = 0.0
vMain = 0.0

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
def updateVoltage():
	global vAux
	global voltageAux

	while True:
		try:
			vAux = adc.read_adc(0, gain=GAIN)
			#vMain = adc.read_adc(0, gain=GAIN)
		except Exception as e:
			print e

		voltageAux = divider1ratio*vAux*0.1875/1000
		# voltageMainBackup = divider2ratio*vMain*0.1875/1000

		time.sleep(.5)

		# print "Main Voltage:"
		# print voltageMainMPPT

		if (voltageAux < 12.15):
			os.system('mpg123 -q lowAux.mp3 &')
		# if (voltageMainBackup < 48.6 or voltageMainMPPT < 48.6):
		# 	os.system('mpg123 -q lowMain.mp3 &')
		print voltageAux

def getAuxV():
    global voltageAux
    return voltageAux
try:
   thread.start_new_thread(updateVoltage,())
except:
   print "Error: unable to start thread"

while True:
	time.sleep(.2)
