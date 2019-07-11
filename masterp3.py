#from __future__ import print_function
import time
# import display
#import batmonitor
# import gpshandler
import shuntcurrent
# import blinker
#import vedirect_m 
import csv
csvfile = open("ADCdata.csv", "a+")
writer = csv.writer(csvfile)

while (True):
  #  global speedM
#    voltageAux = batmonitor.getAuxV()
  #  speedM = gpshandler.getSpeed()
  #  auxV = batmonitor.getAuxV()
  #  mph = speedM*0.621371

  #  mphr = round(mph, 2)
  #  auxVr = round(auxV, 2)


  #  text = str(mphr) + "mph\nAux:" + str(auxVr) + "V"
  #  print text
  #  display.updateDisplay(text)
  
    blinker.updatePins()

    scurrent = shuntcurrent.updateCurrent()
    print(scurrent)
    #a = [0, scurrent]
    #writer.writerow(a)
    file = open('currentdata.txt', 'a+')
    file.write(str(scurrent))
    file.write('\n')
    file.close()

    time.sleep(.5)

csvfile.close()
