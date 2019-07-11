#from __future__ import print_function
import time
# import display
#import batmonitor
# import gpshandler
#import shuntcurrent
import blinker
import vedirect_m 

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
  
    datadict = vedirect_m.run()
    voltageMain = datadict['V']
    #print(voltageMain)
    file = open('voltagedata.txt', 'a+')
    file.write(voltageMain)
    file.write('\n')
    file.close()
    blinker.updatePins()

    time.sleep(.5)
