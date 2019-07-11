#https://github.com/karioja/vedirect/blob/master/vedirect.py
import os
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
import time
import thread
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
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
# GAIN = 1
divider1ratio = 3.3333
divider2ratio = 12

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
	chanp0 = AnalogIn(ads, ADS.P0)
	chanp1 = AnalogIn(ads, ADS.P1)
	voltageAUX = 0
	while True:
		try:
			voltageAux = chanp0.voltage - chanp1.voltage
		except Exception as e:
			print(e)

		# multiplier
                voltageAux *= 69

		if (voltageAux < 12.15):
			os.system('mpg123 -q lowAUX.mp3 &')
		print(voltageAux)
		print(type(voltageAux))
