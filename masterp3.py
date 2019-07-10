#from __future__ import print_function
import time
# import display
#import batmonitor
# import gpshandler
import shuntcurrent
# import blinker
#import vedirect_m 

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
  
  #  blinker.updatePins()
#    scurrent = shuntcurrent.updateCurrent()
#    print(scurrent)
#    voltageMain = vedirect_m.run()
#    print voltageMain

    scurrent = shuntcurrent.updateCurrent()
    print(scurrent)
    file = open('currentdata.txt', 'a+')
    file.write(scurrent)
    file.write('\n')
    file.close()

# write to webpage

    time.sleep(.5)
