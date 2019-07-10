import time


path = "/var/www/html/index.html"
HTML_file = open(path, "w")
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
    voltfile.close()

    intc = int(line)
    intv = int(linev)
    power = intc * intv
    print("power:", power)
    j += 1

    html_str = '''
        <!DOCTYPE html>
        <html>
        <head>
        <title> Monitor</title>
        </head>
        <body>

        <h1> Power Out: <%= power%> </h1>
        <h1> Main Battery Voltage: <%= linev %> </h1>

        </body>
        </html>
    '''

    HTML_file.write(html_str)


HTML_file.close()
