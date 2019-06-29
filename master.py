import time
import display
import batmonitor
import gpshandler

while (True):
    global speedM
    #voltageAux = batmonitor.getAuxV()
    speedM = gpshandler.getSpeed()
    auxV = batmonitor.getAuxV()
    mph = speedM*0.621371

    mphr = round(mph, 2)
    auxVr = round(auxV, 2)

    batmonitor.updateCurrentOut()


    text = str(mphr) + "mph\nAux:" + str(auxVr) + "V"
    print text
    display.updateDisplay(text)
    time.sleep(.5)
