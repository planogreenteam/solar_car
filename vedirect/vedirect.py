#!/usr/bin/python
# -*- coding: utf-8 -*-
# path of Python interpreter added
from __future__ import print_function
from datetime import datetime
import os, serial, argparse, csv



class vedirect:

    def __init__(self, serialport, timeout):
        self.serialport = serialport
        self.ser = serial.Serial(serialport, 19200, timeout=timeout)
        self.header1 = '\r'
        self.header2 = '\n'
        self.hexmarker = ':'
        self.delimiter = '\t'
        self.key = ''
        self.value = ''
        self.bytes_sum = 0;
        self.state = self.WAIT_HEADER
        self.dict = {}

    (HEX, WAIT_HEADER, IN_KEY, IN_VALUE, IN_CHECKSUM) = range(5)

    def input(self, byte):
        if byte == self.hexmarker and self.state != self.IN_CHECKSUM:
            self.state = self.HEX
	
	if self.state == self.WAIT_HEADER:
            self.bytes_sum += ord(byte)
            if byte == self.header1:
                self.state = self.WAIT_HEADER
            elif byte == self.header2:
                self.state = self.IN_KEY

            return None
        elif self.state == self.IN_KEY:
            self.bytes_sum += ord(byte)
            if byte == self.delimiter:
                if self.key == 'Checksum':
                    self.state = self.IN_CHECKSUM
                else:
                    self.state = self.IN_VALUE
            else:
                self.key += byte
            return None
        elif self.state == self.IN_VALUE:
            self.bytes_sum += ord(byte)
            if byte == self.header1:
                self.state = self.WAIT_HEADER
                self.dict[self.key] = self.value;
                self.key = '';
                self.value = '';
            else:
                self.value += byte
            return None
        elif self.state == self.IN_CHECKSUM:
            self.bytes_sum += ord(byte)
            self.key = ''
            self.value = ''
            self.state = self.WAIT_HEADER
            if self.bytes_sum % 256 == 0:
                self.bytes_sum = 0
                return self.dict
            else:
                print
                'Malformed packet'
                self.bytes_sum = 0
        elif self.state == self.HEX:
            self.bytes_sum = 0
            if byte == self.header2:
                self.state = self.WAIT_HEADER
        else:
            raise AssertionError()

    def read_data(self):
        while True:
            byte = self.ser.read(1)
            packet = self.input(byte)

    def read_data_single(self):
        while True:
            byte = self.ser.read(1)
            packet = self.input(byte)
            if packet != None:
                return packet

    def read_data_callback(self, callbackFunction):
        while True:
            byte = self.ser.read(1)
            if byte:
                packet = self.input(byte)
                if packet != None:
                    callbackFunction(packet)
            else:
                break


def print_data_callback(data):
    # print(data)
# data is a dictionary
    output = open('datawrite.csv', 'a+')
    writer = csv.writer(output)  
    writer.writerow([key for key in data.keys()])
    writer.writerow([value for value in data.values()])
#    for key, value in data.items():
#        print(key, value, end=', ')
#        writer.writerow([key, value])
#    print(' ', end='\n')
    output.close()
   # print('Writing Complete')


if __name__ == '__main__':
    try:
       #  print("program started")
    # parser = argparse.ArgumentParser(description='Process VE.Direct protocol')
    # parser.add_argument('--port', help='Serial port')
    # parser.add_argument('--timeout', help='Serial port read timeout', type=int, default='10')
    # args = parser.parse_args()
    #ve = vedirect(args.port, args.timeout)
        ve = vedirect('/dev/ttyUSB0', 60)
#	ve = vedirect('/tmp/vmodem1', 60)
	# with open('datawrite.csv', 'a+') as output:
         #       writer = csv.writer(output)
        # writer.writerow(['LOAD', 'DM', 'ERR', 'FW', 'H21', 'H20', 'H23', 'H22', 'SOC', 'VPV', 'Relay', 'PID', 'H16', 'I', 'BMV', 'PPV', 'TTG', 'Alarm', 'H18', 'H19', 'H10', 'H11', 'H12', 'H13', 'H14', 'VM', 'CE', 'H15', 'P', 'AR', 'SER' , 'V', 'CS', 'H17', 'H8', 'H9', 'H2' , 'H3', 'IL', 'H1', 'H6', 'H7', 'H4', 'H5', 'VS', 'HSDS', 'T', 'TIME_H'])

	ve.read_data_callback(print_data_callback)
    # print(ve.read_data_single())
    except Exception as e:
	errfile = open('/tmp/error.txt', 'w')
	errfile.write(str(e))
	errfile.close()
