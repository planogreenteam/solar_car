import time
import linecache


def line_jump():
    line_offset = []
    offset = 0
    currentfile = open('currentdata.txt', 'r')
    currentfile.close()
j = 0
while True: 

    time.sleep(2)
    currentfile = open('currentdata.txt', 'r')
    lines = currentfile.readlines() 
    line = lines[j]
    print(line)
    currentfile.close()
    voltfile = open('voltagedata.txt', 'r')
    linesv = voltfile.readlines()
    linev = linesv[j]
    print(linev)
    intc = int(line)
    intv = int(linev)
    power = intc * intv
    print("power:", power)
    j += 1
